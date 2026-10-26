# PAS · Privacy Access System

[Deutsch](README.de.md) · [Technical handbook](handbook.en.md) · [Evidence](evidence.en.md) · [FAQ and roadmap](FAQ.en.md)

Documentation prepared on 2026-10-23; personal-project presentation updated on 2026-10-26. Software 0.8.0 · API v1 · schema 6 · `production_ready=false`.

**A personal development project by Leo de Matos, seeking constructive technical feedback.** This repository presents the idea, architecture, historical internal results and open questions. It is not a commercial software offer, supported product launch or open-source release of the PAS Core. Possible future collaboration would be considered separately if interest develops.

PAS explores entitlement, access and recovery under the deploying operator's control, without mandatory email or a mandatory manufacturer identity account. The starting idea is a possession-based entitlement proof, with a convenient account/login layer above it and controlled recovery when credentials are lost. Developers, security specialists and interested readers are invited to challenge the design and its practical limits. DE/EU-first deployment is an operator goal that needs evidence for each actual deployment, not a certification established by this repository.

A typical evaluation follows an issued entitlement proof through activation, convenient login, a protected application action, and controlled recovery or revocation. We seek feedback on that integration journey, identity/role boundaries, recovery risks and operational fit. [Follow the synthetic walkthrough](handbook.en.md#illustrative-walkthrough).

![Access boundaries](figures/boundaries.en.svg)

Login authenticates access; Core manages entitlement and recovery; an application binds an application-specific subject to its own identity and roles. Possession of a code does not identify a real person. The portal does not receive personal C/A/R proofs. [Explore the architecture and synthetic walkthrough](handbook.en.md#architecture).

This is the documentation and technical-review repository for PAS, maintained under `ripitship/pas-privacy-access-system`. Its actual visibility is shown by GitHub's Public/Private label. Use **Issues → New issue** for non-confidential questions, feedback or a review request when you have access. Once this repository is public, those issues are visible to everyone; GitHub does not provide a general private-message inbox. Sensitive findings belong only in the confidential route described in [SECURITY.md](SECURITY.md), never in public issues. Review requests require individual approval and do not grant source access. No separate public project email is currently provided.

The complete PAS source stays private. This repository contains documentation, synthetic figures and a standalone documentation checker, not PAS runtime software or an executable demo. Any private evaluation needs separate approval and agreed terms; no purchase, business-use permission or support contract is offered here. [Publication and rights notice](NOTICE.md).

Leo de Matos is the project initiator and intended project contact. This attribution does not establish sole authorship or ownership of all software, third-party or AI-assisted material. No contact SLA or automatic support service is promised.

Start with [integration and risks](handbook.en.md#integration), [dated internal evidence](evidence.en.md), then [requesting a private review](REVIEW.md). Sensitive findings follow [SECURITY.md](SECURITY.md).
