# Datierte interne Nachweise

[Start](README.de.md) · [English](evidence.en.md) · [Maschinenlesbare Projektion](evidence.json)

Alle folgenden Softwareergebnisse sind historische interne Ergebnisse vom 06.10.2026, keine für diese Dokumentationsvorbereitung am 23.10.2026 neu ausgeführten PAS-Tests. Sie betreffen Software 0.8.0, API v1, Schema 6, `production_ready=false`. Sie sind kein externes Audit, keine Produktionszertifizierung, Hardwarefreigabe oder Herstelleridentitäts-Attestation.

| Historischer Umfang | Berichtetes Ergebnis |
| --- | --- |
| Vollständige Regression, Darwin ARM64, Python 3.12.14 | 665 bestanden, 0 übersprungen, 2 bestehende Abkündigungswarnungen aus Abhängigkeiten |
| Natives Linux ARM64, Python 3.12.3 | 53 Checks bestanden; synthetisches natives Loopback |
| Separate unabhängige App20-Umgebung | 20 exakte Distributionen; 8 App-Checks bestanden; allein kein authentisierter Loginbeleg |
| OCI Linux ARM64 | 24 Funktions- und 9 Containerchecks bestanden; vier Container/fünf Listener; Images Python 3.12.15, Gastcontroller Python 3.12.3 |

Das bereinigte JSON fasst die privat aufbewahrten Berichte strikt zusammen. Es enthält Hashes der ursprünglichen privaten Evaluations- und App-Quellarchive zur Zuordnung des Nachweises, aber keinen Archivdownload oder Laufzeitzustand. Quellsignaturen nutzten einen flüchtigen Testsigner und separat gepinnten Testanker; sie attestieren keine kommerzielle Herstelleridentität oder spätere Image-Builds.

Vollständiger Code, Rohberichte, exakte Originalarchive und Reproduktionsvoraussetzungen erfordern ein individuell freigegebenes privates Review. Öffentliche Leser können die PAS-Suite aus diesem reinen Dokumentationsbaum nicht reproduzieren. Aktuelle Dokumentationschecks prüfen nur Veröffentlichungsgrenzen, lokale Links und Grafiken. Erfolgreiche Dokumentations-CI ist kein PAS-Testbadge.

Eine frische private Evaluation braucht vereinbarten Umfang, vertrauenswürdiges Python/Abhängigkeiten, synthetischen privaten Zustand, betreiberkontrollierte Schlüssel und freigegebenes Hosting. Linux x86_64, Windows, beliebige Engines, reale Browser-/Hardwareabdeckung, echter P1-48-Stunden-Lauf, unabhängiges HSM/HA und Produktionsbetrieb bleiben unbelegt.
