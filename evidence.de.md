# Datierte interne Nachweise

[Start](README.de.md) · [English](evidence.en.md) · [Maschinenlesbare Projektion](evidence.json)

## Kontrollierte interne Evaluation · 23. November 2026

Software 0.8.0 · API v1 · Schema 6 · `production_ready=false`. Für die Dokumentationsaktualisierung am 24. November wurden die gespeicherten Ergebnisse und alle 111 Dateien des festgehaltenen Quellmanifests geprüft. Die angegebenen PAS-Läufe fanden am 23. November statt.

| Umfang | Festgehaltenes Ergebnis |
| --- | --- |
| Vollständige PAS-Suite | 1.118 bestanden, 14 übersprungen, 0 Fehlschläge oder Fehler, 2 bestehende Abhängigkeitswarnungen |
| Node-Oberflächentests | 31 bestanden |
| Neue HTTP-Integrationsfälle | 3 bestanden und im PAS-Gesamtlauf enthalten |
| Lokale native Loopback-Prüfung | Core 21/21, Integrationslabor 24/24 |

Die Zahlen überlappen. Die Browserbeobachtung nutzte synthetische Daten und erfasste Standardlogin, Guardian-Status, Tastaturfokus, Abmeldung sowie eine 390 Pixel breite Ansicht ohne horizontalen Überlauf. Die Nutzung physischer Authenticatoren, tatsächliche Guardian-Bindung und vollständige Recovery im Browser sind ungeprüft.

KI-gestützte Reviewer haben die Änderungen innerhalb des Projekts unabhängig geprüft. Ein externes Audit, unabhängig geprüfte Schlüsselverwahrung, Hardware- und Produktionsfreigabe stehen noch aus. P2 bleibt gesperrt.

## Historische interne Evaluation · 6. Oktober 2026

Diese Ergebnisse beziehen sich auf die Oktoberevaluation von Software 0.8.0, API v1 und Schema 6. Sie belegen für diesen Zeitpunkt folgende plattformspezifische Ergebnisse.

| Historischer Umfang | Berichtetes Ergebnis |
| --- | --- |
| Vollständige Regression, Darwin ARM64, Python 3.12.14 | 665 bestanden, 0 übersprungen, 2 bestehende Abkündigungswarnungen aus Abhängigkeiten |
| Natives Linux ARM64, Python 3.12.3 | 53 Checks bestanden; synthetisches natives Loopback |
| Separate unabhängige App20-Umgebung | 20 exakte Distributionen; 8 App-Checks bestanden; allein kein authentisierter Loginbeleg |
| OCI Linux ARM64 | 24 Funktions- und 9 Containerchecks bestanden; vier Container/fünf Listener; Images Python 3.12.15, Gastcontroller Python 3.12.3 |

Im JSON beschreibt `current_evaluation` die Novemberergebnisse. Die historischen Felder und privaten Archiv-Hashes gehören zur Oktoberevaluation und ihren ursprünglichen privaten Evaluations- und Beispiel-App-Archiven. Die Oktobersignaturen verwendeten einen flüchtigen Testsigner und einen separat festgelegten Testanker. Herstelleridentität und spätere Image-Builds liegen außerhalb dieses Nachweises.

Vollständiger Quellcode, Originalarchive, Rohberichte und Reproduktionsvoraussetzungen erfordern ein individuell freigegebenes privates Review. Die GitHub-CI prüft den öffentlichen Dateibestand, lokale Links, Grafiken und fest hinterlegte Nachweisdaten. Für die Reproduktion der PAS-Ergebnisse sind die private Umgebung und ein gesondert vereinbarter Umfang erforderlich.

Eine frische private Evaluation braucht vertrauenswürdiges Python und geprüfte Abhängigkeiten, synthetischen Zustand, betreiberkontrollierte Schlüssel und freigegebenes Hosting. Linux x86_64, Windows, andere Engines, ein echter 48-Stunden-P1-Lauf, unabhängiges HSM und Hochverfügbarkeit sind ungeprüft.
