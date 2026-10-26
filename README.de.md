# PAS · Privacy Access System

[English](README.md) · [Technischer Leitfaden](handbook.de.md) · [Nachweise](evidence.de.md) · [FAQ und Roadmap](FAQ.de.md)

Dokumentation vorbereitet am 23.10.2026; Vorstellung als persönliches Projekt aktualisiert am 26.10.2026. Software 0.8.0 · API v1 · Schema 6 · `production_ready=false`.

**Ein persönliches Entwicklungsprojekt von Leo de Matos, das konstruktives fachliches Feedback sucht.** Dieses Repository stellt Grundidee, Architektur, historische interne Ergebnisse und offene Fragen vor. Es ist kein kommerzielles Softwareangebot, unterstützter Produktstart oder Open-Source-Release des PAS-Kerns. Mögliche spätere Zusammenarbeit wird bei tatsächlichem Interesse gesondert betrachtet.

PAS untersucht Berechtigungen, Zugang und Recovery unter Kontrolle des jeweiligen Betreibers, ohne Pflicht-E-Mail oder obligatorisches Hersteller-Identitätskonto. Ausgangspunkt ist ein besitzbasierter Berechtigungsnachweis mit einer nutzerfreundlichen Konto-/Login-Schicht darüber und kontrollierter Wiederherstellung bei verlorenen Zugangsdaten. Entwickler, Security-Fachleute und interessierte Leser sind eingeladen, den Entwurf und seine praktischen Grenzen kritisch zu prüfen. DE/EU-first ist ein Betriebsziel, das für jede tatsächliche Bereitstellung belegt werden muss, keine durch dieses Repository erwiesene Zertifizierung.

Eine typische Evaluation folgt einem ausgegebenen Berechtigungsnachweis über Aktivierung, bequemen Login und eine geschützte Anwendungsaktion bis zu kontrollierter Recovery oder Widerruf. Gesucht ist Feedback zu diesem Integrationsablauf, Identitäts-/Rollengrenzen, Recovery-Risiken und betrieblicher Eignung. [Synthetischen Ablauf verfolgen](handbook.de.md#illustrativer-ablauf).

![Zugangsgrenzen](figures/boundaries.de.svg)

Login authentisiert den Zugang; Core verwaltet Berechtigungen und Recovery; eine Anwendung ordnet einen anwendungsspezifischen Subject ihrer eigenen Identität und ihren Rollen zu. Codebesitz identifiziert keine reale Person. Das Portal erhält keine persönlichen C/A/R-Nachweise. [Architektur und synthetischen Ablauf ansehen](handbook.de.md#architektur).

Dies ist das Dokumentations- und technische Review-Repository für PAS unter `ripitship/pas-privacy-access-system`. Die tatsächliche Sichtbarkeit zeigt GitHub mit dem Kennzeichen Public/Private an. Für nicht vertrauliche Fragen, Feedback oder Review-Anfragen **Issues → New issue** verwenden, sobald Zugang besteht. Bei öffentlichem Repository sind diese Issues für alle sichtbar; GitHub bietet keinen allgemeinen privaten Nachrichteneingang. Sensible Befunde gehören ausschließlich in den unter [SECURITY.md](SECURITY.md) beschriebenen vertraulichen Weg, niemals in öffentliche Issues. Review-Anfragen brauchen eine individuelle Freigabe und gewähren keinen Quellzugang. Eine separate öffentliche Projekt-E-Mail wird derzeit nicht angegeben.

Der vollständige PAS-Quellcode bleibt privat. Dieses Repository enthält Dokumentation, synthetische Grafiken und einen eigenständigen Dokumentationsprüfer, keine PAS-Laufzeitsoftware oder ausführbare Demo. Eine private Evaluation braucht gesonderte Freigabe und vereinbarte Bedingungen; Kauf, geschäftliche Nutzungsfreigabe oder Supportvertrag werden hier nicht angeboten. [Veröffentlichungs- und Rechtehinweis](NOTICE.md).

Leo de Matos ist Projektinitiator und vorgesehener Projektkontakt. Diese Zuordnung belegt keine alleinige Urheberschaft oder Rechteinhaberschaft an sämtlicher Software sowie fremden oder KI-unterstützten Materialien. Kontakt-SLA oder automatischer Support werden nicht zugesagt.

Einstieg: [Integration und Risiken](handbook.de.md#integration), [datierte interne Nachweise](evidence.de.md), dann [privates Review anfragen](REVIEW.md). Sensible Befunde richten sich nach [SECURITY.md](SECURITY.md).
