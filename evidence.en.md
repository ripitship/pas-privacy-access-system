# Dated internal evidence

[Home](README.md) · [Deutsch](evidence.de.md) · [Machine-readable projection](evidence.json)

## Controlled internal evaluation · 23 November 2026

Software 0.8.0 · API v1 · schema 6 · `production_ready=false`. The 24 November documentation refresh checked the retained results and all 111 files in the frozen source manifest. The reported PAS runs took place on 23 November.

| Scope | Recorded result |
| --- | --- |
| Full PAS suite | 1,118 passed, 14 skipped, 0 failures or errors, 2 existing dependency warnings |
| Node UI behavior | 31 passed |
| New HTTP integration cases | 3 passed within the full PAS suite |
| Local native loopback | Core 21/21, integration lab 24/24 |

The counts overlap. The browser observation used synthetic data and covered standard login, Guardian status, keyboard focus, logout and a 390-pixel viewport without horizontal overflow. Physical authenticator use, live Guardian binding and full recovery in the browser remain unverified.

AI-assisted reviewers assessed the changes independently within the project. An external audit, independently verified key custody, hardware approval and production approval remain open. P2 is blocked.

## Historical internal evaluation · 6 October 2026

These results refer to the October evaluation of software 0.8.0, API v1 and schema 6. They establish the following platform-specific evidence for that date.

| Historical scope | Reported outcome |
| --- | --- |
| Complete regression, Darwin ARM64, Python 3.12.14 | 665 passed, 0 skipped, 2 existing dependency deprecation warnings |
| Native Linux ARM64, Python 3.12.3 | 53 checks passed; synthetic native loopback |
| Separate independent App20 environment | 20 exact distributions; 8 application checks passed; not authenticated login proof alone |
| OCI Linux ARM64 | 24 functional and 9 container checks passed; four containers/five listeners; images Python 3.12.15, guest controller Python 3.12.3 |

In the JSON, `current_evaluation` describes the November results. The historical fields and private archive hashes identify the October evaluation and its original private evaluation and sample App archives. The October test signatures used an ephemeral signer and a separately pinned test anchor. Manufacturer identity and later image builds lie outside that evidence.

Individually approved private review is required to access the complete source, original archives, raw results and reproduction prerequisites. GitHub CI validates the public file inventory, local links, figures and pinned evidence. Reproducing the PAS results requires the private environment and a separately agreed scope.

A fresh private evaluation needs trusted Python and dependencies, synthetic state, operator-controlled keys and approved hosting. Linux x86_64, Windows, other engines, a real 48-hour P1 run, independent HSM and high availability remain unverified.
