"""Offline standard-library documentation checker; not a PAS test or full secret scan.

FILES is the fixed public allowlist. Hashes detect drift, not authorship. Review
changes manually before refreshing inventory. Diagnostics never print contents.
"""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

FILES = tuple(sorted([
    'README.md', 'README.de.md', 'handbook.en.md', 'handbook.de.md',
    'evidence.en.md', 'evidence.de.md', 'evidence.json', 'FAQ.en.md', 'FAQ.de.md',
    'NOTICE.md', 'REVIEW.md', 'SECURITY.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md',
    'figures/boundaries.en.svg', 'figures/boundaries.de.svg',
    'figures/access.en.svg', 'figures/access.de.svg',
    'figures/recovery.en.svg', 'figures/recovery.de.svg',
    '.github/ISSUE_TEMPLATE/config.yml', '.github/ISSUE_TEMPLATE/question.yml',
    '.github/ISSUE_TEMPLATE/feedback.yml', '.github/ISSUE_TEMPLATE/review.yml',
    '.github/ISSUE_TEMPLATE/partnership.yml', '.github/workflows/documentation.yml',
    'tools/check_public.py',
]))
WORKFLOW = '''name: Documentation only
on: [push, pull_request]
permissions:
  contents: read
jobs:
  documentation:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1
        with:
          persist-credentials: false
      - name: Validate public documentation only
        run: python3 tools/check_public.py . --repository
'''
EXPECTED_EVIDENCE = {
    'evidence_date': '2026-10-06',
    'classification': 'historical internal results; sanitized projection; not rerun on preparation date',
    'software_version': '0.8.0', 'api': 'v1', 'schema': 6, 'production_ready': False,
    'regression': {'system': 'Darwin', 'machine': 'arm64', 'python': '3.12.14', 'passed': 665, 'skipped': 0, 'warnings': 2},
    'native_linux': {'system': 'Linux', 'machine': 'aarch64', 'python': '3.12.3', 'checks_passed': 53},
    'independent_app': {'exact_distributions': 20, 'checks_passed': 8, 'authenticated_login_proof_alone': False},
    'oci': {'system': 'Linux', 'machine': 'aarch64', 'functional_checks': 24, 'container_checks': 9, 'image_python': '3.12.15', 'guest_controller_python': '3.12.3'},
    'private_archive_sha256': {'evaluation': '26fb0dab0a4ea64f96b97c2982f6472ef61f0ff9c6ad92e31feac0d816d73ca9', 'application': 'b7f6f40f6cdb583618513155e4069c84e6d379cfd431292b5f58bea933c6d354'},
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inventory(root):
    return ''.join(f'{digest(root / name)}  {name}\n' for name in FILES)

def write_inventory(root):
    (root / 'SHA256SUMS.txt').write_text(inventory(root), encoding='utf-8')

def slug(text):
    return ''.join(c for c in text.lower().replace(' ', '-')
                   if c in '-_' or unicodedata.category(c)[0] in 'LN')

def validate(root, require_inventory=True, repository=False):
    root = Path(root)
    errors = []
    def fail(code, name='.'):
        errors.append(f'{code}: {name}')
    if root.is_symlink() or not root.is_dir():
        return ['invalid public root']
    root = root.resolve()
    expected = set(FILES)
    if require_inventory or (root / 'SHA256SUMS.txt').exists():
        expected.add('SHA256SUMS.txt')
    actual = set()
    allowed_dirs = {str(p) for n in FILES for p in PurePosixPath(n).parents if str(p) != '.'}
    def walk(folder):
        for p in sorted(folder.iterdir()):
            name = p.relative_to(root).as_posix()
            if p.is_symlink():
                fail('symlink rejected', name)
            elif p.is_dir():
                if repository and folder == root and name == '.git':
                    continue
                if name not in allowed_dirs:
                    fail('unexpected directory', name)
                walk(p)
            elif p.is_file():
                actual.add(name)
            else:
                fail('special file rejected', name)
    walk(root)
    for name in sorted(actual - expected):
        fail('unexpected file', name)
    for name in sorted(expected - actual):
        fail('missing file', name)
    if errors:
        return errors
    contents = {}
    for name in sorted(actual):
        try:
            data = (root / name).read_bytes()
            if len(data) > 200000:
                fail('oversized file', name); continue
            text = data.decode('utf-8')
            contents[name] = text
            if '\x00' in text or data.startswith((b'PK\x03\x04', b'SQLite format')):
                fail('binary or runtime artifact', name)
            if re.search(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}', text):
                fail('email rejected', name)
            machine = r'/(?:Users|home|private|tmp|var)/|(?<![A-Za-z])[A-Za-z]:[\\/]'
            if re.search(machine, text):
                fail('machine path rejected', name)
            if any(token in text for token in ['BEGIN ' + 'PRIVATE KEY', 'BEGIN RSA ' + 'PRIVATE KEY', 'from pas_' + 'local import']):
                fail('private material marker', name)
        except (UnicodeError, OSError):
            fail('unreadable text', name)
    if errors:
        return errors
    if contents['.github/workflows/documentation.yml'] != WORKFLOW:
        fail('workflow differs from least-privilege approved policy', '.github/workflows/documentation.yml')
    try:
        if json.loads(contents['evidence.json']) != EXPECTED_EVIDENCE:
            fail('archival evidence changed', 'evidence.json')
    except ValueError:
        fail('invalid evidence JSON', 'evidence.json')
    for name, text in contents.items():
        if name.endswith('.md'):
            for raw in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
                target = urlsplit(raw)
                if target.scheme or target.netloc or target.query:
                    fail('nonlocal link rejected', name); continue
                decoded = unquote(target.path)
                if decoded.startswith(('/', '\\')) or '\\' in decoded:
                    fail('absolute link rejected', name); continue
                path = (root / name).parent / decoded if decoded else root / name
                resolved = path.resolve()
                if not resolved.is_relative_to(root):
                    fail('link escapes public root', name)
                elif not resolved.is_file():
                    fail('broken local link', name)
                elif target.fragment:
                    linked = resolved.read_text(encoding='utf-8')
                    anchors = {slug(h) for h in re.findall(r'^#{1,6} (.+)$', linked, re.M)}
                    if unquote(target.fragment) not in anchors:
                        fail('broken local anchor', name)
        if name.endswith('.svg'):
            try:
                svg = ET.fromstring(text)
                tags = {'svg', 'g', 'rect', 'text', 'title', 'desc'}
                if svg.tag != '{http://www.w3.org/2000/svg}svg' or not svg.get('viewBox'):
                    fail('invalid SVG root', name)
                for el in svg.iter():
                    if el.tag.split('}')[-1] not in tags:
                        fail('active or unsupported SVG element', name)
                    if any(k.lower().startswith('on') or 'href' in k.lower() or 'url(' in v.lower() for k,v in el.attrib.items()):
                        fail('active or external SVG attribute', name)
                if not svg.findtext('{http://www.w3.org/2000/svg}title') or not svg.findtext('{http://www.w3.org/2000/svg}desc'):
                    fail('missing SVG accessible label', name)
            except ET.ParseError:
                fail('invalid SVG XML', name)
    for name in ['README.md', 'README.de.md']:
        if 'Leo de Matos' not in contents[name] or 'production_ready=false' not in contents[name]:
            fail('required attribution/status missing', name)
    if require_inventory and contents['SHA256SUMS.txt'] != inventory(root):
        fail('SHA256 inventory mismatch', 'SHA256SUMS.txt')
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', default='.')
    parser.add_argument('--refresh-inventory', action='store_true', help='After manual review: refresh hashes, then validate')
    parser.add_argument('--repository', action='store_true', help='CI only: ignore the real root .git directory, never symlinks; export mode stays strict')
    args = parser.parse_args()
    root = Path(args.root)
    if args.refresh_inventory:
        problems = validate(root, require_inventory=False, repository=args.repository)
        if problems:
            print(json.dumps({'status':'failed', 'findings':problems}, indent=2)); return 1
        write_inventory(root)
    problems = validate(root, repository=args.repository)
    print(json.dumps({'status':'failed' if problems else 'passed', 'scope':'documentation only; bounded checks, not full secret scanning', 'files':len(FILES)+1, 'findings':problems}, indent=2))
    return int(bool(problems))

if __name__ == '__main__':
    sys.exit(main())
