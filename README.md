# PAS · Privacy Access System

[Deutsch](README.de.md) · [Technical handbook](handbook.en.md) · [Evidence](evidence.en.md) · [FAQ and roadmap](FAQ.en.md)

Documentation prepared on 2026-10-23; private repository staging updated on 2026-10-26. Software 0.8.0 · API v1 · schema 6 · `production_ready=false`.

PAS explores entitlement, access and recovery under the customer's operational control, without mandatory email or a mandatory manufacturer identity account. IT consultants, service providers and integrators can assess whether this model fits their own customer workflows. DE/EU-first deployment is an operator goal that needs evidence for each actual deployment.

A typical evaluation follows an issued entitlement proof through activation, convenient login, a protected application action, and controlled recovery or revocation. We seek feedback on that integration journey, identity/role boundaries, recovery risks and operational fit. [Follow the synthetic walkthrough](handbook.en.md#illustrative-walkthrough).

![Access boundaries](figures/boundaries.en.svg)

Login authenticates access; Core manages entitlement and recovery; an application binds an application-specific subject to its own identity and roles. Possession of a code does not identify a real person. The portal does not receive personal C/A/R proofs. [Explore the architecture and synthetic walkthrough](handbook.en.md#architecture).

This is the documentation and technical-review repository for PAS, maintained under `ripitship/pas-privacy-access-system`. It is currently staged privately while publication, rights and contact requirements are clarified. After public launch and channel setup, ordinary non-confidential questions, feedback, review and partnership requests may use repository issues. A confidential security reporting route must be configured before launch; none is claimed to be operational yet. Review requests require individual approval and do not grant source access.

The complete PAS source stays private. Free technical evaluation is intended under agreed review terms; permanent business use requires agreement. This is not a free open-source software release, executable demo or production certification. [Publication and rights notice](NOTICE.md).

Leo de Matos is the project initiator and intended project contact. This attribution does not establish sole authorship or ownership of all software, third-party or AI-assisted material. No contact SLA or automatic support service is promised.

Start with [integration and risks](handbook.en.md#integration), [dated internal evidence](evidence.en.md), then [requesting a private review](REVIEW.md). Sensitive findings follow [SECURITY.md](SECURITY.md).
