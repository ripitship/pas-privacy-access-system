# PAS · Privacy Access System

[Deutsch](README.de.md) · [Architecture](handbook.en.md#architecture) · [Join the review](https://github.com/ripitship/pas-privacy-access-system/issues)

**Can access and account recovery work without making email the mandatory anchor?** PAS explores a possession-based entitlement proof, with a convenient login layer above it and recovery rules under the deploying operator's control.

Personal development project by Leo de Matos. **Prototype, not production-ready.** PAS Core source remains private; this public repository is for architecture discussion and documentation feedback, not an executable PAS release.

## Why explore this?

The design separates three questions: **Are you entitled? How do you log in? Who are you allowed to act as in this application?** Not every service needs an email address to answer them. Some still need a verified business identity; the application must establish that identity and its roles explicitly.

The intended operator controls hosting, keys, recovery policy, identity mapping and update approval. DE/EU-first operation is a deployment goal, not a certification or a claim of independence established by placing documents on GitHub. GitHub is not a required PAS runtime identity service.

## Start in five minutes

- Follow [one synthetic access and recovery journey](handbook.en.md#illustrative-walkthrough). No installation or PAS account is needed to read it.
- Inspect [the trust boundaries and integration contract](handbook.en.md#architecture).
- Pick [one review question](REVIEW.md#three-starting-questions) and [join the conversation](https://github.com/ripitship/pas-privacy-access-system/issues). A short, specific objection is useful; you do not need to audit the whole project.

## How the pieces fit

![Access boundaries](figures/boundaries.en.svg)

Login authenticates access; Core manages entitlement and recovery; an application binds an application-specific subject to its own identity and roles. Possession of a code does not identify a real person. The portal does not receive personal C/A/R proofs. [Explore the architecture](handbook.en.md#architecture).

## Help us challenge the design

1. **Identity boundary:** where would your application need a real identity rather than an entitlement proof?
2. **Recovery:** which loss cases should fail closed instead of permitting a reset?
3. **Integration:** what protocol, role binding and operational evidence would you require before a supervised evaluation?

[Discuss an existing question](https://github.com/ripitship/pas-privacy-access-system/issues) or [ask your own](https://github.com/ripitship/pas-privacy-access-system/issues/new/choose). Please use generic or synthetic examples. Ordinary questions need no private-review agreement. Sensitive findings follow [SECURITY.md](SECURITY.md), never public comments.

## What is established, and what is not?

Software 0.8.0 · API v1 · schema 6 · `production_ready=false`. Historical internal software results are dated 2026-10-06; the current GitHub checks validate documentation only. They are not an independent security audit. [Evidence and reproducibility limits](evidence.en.md).

Joint theft of the possession and recovery proofs is a stated P0 risk. Total loss cannot safely be recovered without admissible independent proof. Higher-assurance recovery depends on actual passkey, guardian, warning and key-isolation arrangements; P2 remains blocked. No complete anonymity, universal platform compatibility or production approval is claimed. [Recovery and deployment limits](handbook.en.md#recovery).

## Source, participation and possible future collaboration

The complete PAS source stays private. This repository contains documentation, synthetic figures and a standalone documentation checker. Public readers can critique the design, but cannot reproduce or audit the private PAS implementation from this tree. Individually approved private evaluations require separately agreed scope and terms. [Review process](REVIEW.md) · [Contribution guide](CONTRIBUTING.md).

If the problem matters in your work, describe the generic workflow and what a satisfactory solution would need to prove. Possible future collaboration can be considered separately; this personal project is not a commercial offer or support service. Leo de Matos is the project initiator and contact through GitHub. Attribution and reuse limits are explained in the [rights notice](NOTICE.md).

Presentation updated on 2026-10-27. [FAQ and development roadmap](FAQ.en.md).
