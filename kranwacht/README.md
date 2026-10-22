# KranWacht Offshore – Prototyp

Klickbarer Prototyp eines Maintenance Tools für Offshore-Krane. Er dient dazu, Hypothesen zu den Bedürfnissen von Maintenance Manager und Service Engineer zu überprüfen.

**Starten:** `index.html` im Browser öffnen. Es ist kein Build nötig. Die Datei lädt d3 und topojson von cdnjs und Schriften von Google Fonts, die Kartendaten sind eingebettet. Alle Daten sind Beispieldaten.

## Was das Tool macht

Das Tool liefert Basisdaten zum Zustand der Krane. Planung und Bestellung finden im eigenen CMMS oder in SAP statt.

| Bereich | Inhalt |
|---|---|
| Flotte | Handlungsbedarf, Weltkarte mit Standorten, Status je Kran, letzte Datenverbindung mit Hinweis bei veralteten Daten |
| Ereignisse | Automatische Zustandsanalysen und manuelle Meldungen in einem Kanal. Fallakte mit Risikobewertung, Wo, Warum, Wie, Dauer, Ausfall, Teile und Werkzeug (für den Service Engineer) |
| Einsatzberichte | Der Service Engineer erfasst das Ergebnis, der Manager schließt den Fall ab oder legt einen Folgefall an |
| Kranakte | Servicehistorie und Hinweis auf wiederkehrende Befunde |
| Nachweise | Durchgeführte Reparaturen und Prüfungen, Export als CSV, JSON oder SAP-PM-IDoc |
| Benachrichtigungen | Regeln je Ereignis und Kanal (App, E-Mail, SMS, Teams) |
| Schnittstelle | REST-API, Webhooks, Zuordnung zu SAP PM |

Oben rechts lässt sich zwischen den Rollen **Maintenance Manager** und **Service Engineer** wechseln.

## Bewusst nicht enthalten

- Restlebensdauer nach Betriebsstunden
- Schiffsentladungen
- Einsatzplanung und Bestellungen
