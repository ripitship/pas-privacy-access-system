# Dated internal evidence

[Home](README.md) · [Deutsch](evidence.de.md) · [Machine-readable projection](evidence.json)

All software results below are historical internal results dated 2026-10-06, not PAS tests rerun for this documentation preparation on 2026-10-23. They concern software 0.8.0, API v1, schema 6, `production_ready=false`. They are not an external audit, production certification, hardware approval or manufacturer identity attestation.

| Historical scope | Reported outcome |
| --- | --- |
| Complete regression, Darwin ARM64, Python 3.12.14 | 665 passed, 0 skipped, 2 existing dependency deprecation warnings |
| Native Linux ARM64, Python 3.12.3 | 53 checks passed; synthetic native loopback |
| Separate independent App20 environment | 20 exact distributions; 8 application checks passed; not authenticated login proof alone |
| OCI Linux ARM64 | 24 functional and 9 container checks passed; four containers/five listeners; images Python 3.12.15, guest controller Python 3.12.3 |

The sanitized JSON is a strict summary of retained private reports. It includes hashes of the original private evaluation and App source archives to identify the evidence scope, but no archive download or runtime state. Source signatures used an ephemeral test signer and a separately pinned test anchor; they do not attest a commercial manufacturer identity or later image builds.

The complete source, raw reports, exact original archives and reproduction prerequisites require individually approved private review. Public readers cannot reproduce the PAS suite from this documentation-only tree. Current documentation checks validate publication boundaries, local links and figures only. A successful documentation CI run is not a PAS test badge.

A fresh private evaluation needs an agreed scope, trusted Python/dependencies, synthetic private state, operator-controlled keys and approved hosting. Linux x86_64, Windows, arbitrary engines, real browser/hardware coverage, a real P1 48-hour run, independent HSM/HA and production operation remain unestablished.
