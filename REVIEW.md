# Technical feedback and review / Fachliches Feedback und Review

You can help without reviewing the private software. Pick one question below, read the linked section, and share a concrete concern or a generic integration requirement. Public architecture feedback needs no private-review agreement. A source-code evaluation is a different, individually approved process.

Du kannst helfen, ohne die private Software zu prüfen. Wähle eine Frage, lies den verlinkten Abschnitt und nenne einen konkreten Einwand oder eine allgemeine Integrationsanforderung. Öffentliches Architekturfeedback braucht keine private Review-Vereinbarung. Eine Quellcode-Evaluation ist ein anderer, einzeln freizugebender Vorgang.

## Three starting questions

1. **Entitlement versus identity:** where must an application bind a PAS subject to a verified person or organisation? What must PAS never infer from a possession proof? Start with [architecture](handbook.en.md#architecture).
2. **Recovery without email:** which independent evidence and warning/veto arrangements would you accept, and when should total loss remain unrecoverable? Start with [recovery limits](handbook.en.md#recovery). Do not publish exploit details.
3. **Integration in an existing portal:** what protocol, role binding, revocation behaviour, key custody and deployment evidence would you need before a supervised evaluation? Start with [integration](handbook.en.md#integration). Compatibility is a question, not a claimed universal adapter.

[See the public questions](https://github.com/ripitship/pas-privacy-access-system/issues) or [open your own](https://github.com/ripitship/pas-privacy-access-system/issues/new/choose). A useful reply can be three lines: a generic scenario, one missing assumption, and what you would need to verify. No customer identities, credentials, secrets or sensitive findings.

## Drei Einstiegsfragen

1. **Berechtigung und Identität:** Wo muss eine Anwendung einen PAS-Subject einer geprüften Person oder Organisation zuordnen? Was darf PAS niemals aus Codebesitz ableiten? Einstieg: [Architektur](handbook.de.md#architektur).
2. **Recovery ohne E-Mail:** Welche unabhängigen Nachweise und Warn-/Veto-Vorkehrungen wären akzeptabel, und wann muss Totalverlust nicht wiederherstellbar bleiben? Einstieg: [Recovery-Grenzen](handbook.de.md#recovery). Keine Exploit-Details veröffentlichen.
3. **Integration in ein vorhandenes Portal:** Welche Protokolle, Rollenzuordnungen, Widerrufsregeln, Schlüsselverwahrung und Betriebsnachweise brauchst du vor einer begleiteten Evaluation? Einstieg: [Integration](handbook.de.md#integration). Kompatibilität ist hier eine Frage, keine behauptete universelle Anbindung.

[Öffentliche Fragen ansehen](https://github.com/ripitship/pas-privacy-access-system/issues) oder [eine eigene eröffnen](https://github.com/ripitship/pas-privacy-access-system/issues/new/choose). Drei Zeilen reichen: allgemeines Szenario, eine fehlende Annahme und der erforderliche Nachweis. Keine Kundenidentitäten, Zugangsdaten, Geheimnisse oder sensiblen Befunde.

## Private evaluation and contact boundaries

Use the issue forms for non-confidential questions, feedback, review requests or possible future collaboration. This is a personal development project, not a sales or customer-support channel. Describe a generic integration, desired review scope and relevant expertise without customer details, personal data, secrets, source excerpts or sensitive findings. Issues are public when the repository is public. No separate public email or general GitHub private-message feature is provided. A confidential business or personal conversation needs a separately agreed channel, not a vulnerability report.

Leo de Matos must individually approve each private review. A request grants no code access. Scope, confidentiality, permitted evaluation, retention/deletion, disclosure, liability and permanent business use need separate agreement and professional review. Access should be limited and removable; a specific private channel is granted separately. No SLA or automatic support is offered. Use [security policy](SECURITY.md) for sensitive findings.

Die Issue-Formulare dienen nicht vertraulichen Fragen, Feedback, Review-Anfragen oder möglicher späterer Zusammenarbeit. Dies ist ein persönliches Entwicklungsprojekt, kein Vertriebs- oder Kundensupportkanal. Allgemeine Integration, gewünschten Review-Umfang und Erfahrung ohne Kundendetails, personenbezogene Daten, Geheimnisse, Quellauszüge oder sensible Befunde beschreiben. Bei öffentlichem Repository sind Issues öffentlich. Eine separate öffentliche E-Mail oder allgemeine private GitHub-Nachrichtenfunktion wird nicht angeboten. Vertrauliche geschäftliche oder persönliche Gespräche brauchen einen separat vereinbarten Kanal, keine Schwachstellenmeldung.

Leo de Matos muss jedes private Review individuell freigeben. Eine Anfrage gewährt keinen Codezugang. Umfang, Vertraulichkeit, erlaubte Evaluation, Aufbewahrung/Löschung, Offenlegung, Haftung und dauerhafte Geschäftsnutzung brauchen separate Vereinbarung und professionelle Prüfung. Zugang soll begrenzt und entziehbar sein; ein konkreter privater Kanal wird separat gewährt. Kein SLA oder automatischer Support. Sensible Befunde richten sich nach der [Sicherheitsrichtlinie](SECURITY.md).
