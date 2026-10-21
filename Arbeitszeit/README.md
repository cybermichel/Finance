# Arbeitszeit

Kleine Web-App zum Erfassen der Arbeitszeit pro Monat – nach dem Vorbild der Excel-Tabelle.

**Öffnen:** `index.html` im Browser öffnen (Doppelklick genügt, keine Installation nötig).

## Was sie kann
- Datum, Kommen, Gehen und Pause (Minuten) eintragen – die Arbeitszeit wird sofort berechnet.
- Pro Monat: gearbeitete Stunden, Sollstunden (Standard 36:50), Überstunden diesen Monat.
- Minusstunden werden negativ (rot) angezeigt.
- **Überstunden Vormonat:** wird automatisch aus dem Ergebnis des Vormonats übernommen. Für Oktober 2026 ist September mit 3:35 vorbelegt; das Feld kann jederzeit überschrieben werden.
- **Genommene Überstunden:** werden vom Gesamtsaldo abgezogen.
- Einträge per Klick bearbeiten, mit × löschen; Monate mit ‹ › wechseln.
- CSV-Export (für Excel), PDF-Export (nur Einträge und Monatsübersicht), Backup sichern und laden.

Zeiten in den Feldern als `h:mm` eingeben, z. B. `3:35` oder `-1:15` (auch `3,5` geht).

**Wichtig:** Die Daten liegen nur im Browser auf diesem Gerät. Regelmäßig „Backup sichern“ klicken.
