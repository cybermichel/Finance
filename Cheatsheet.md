# Cheatsheet: Finanz-Plugins in Claude Code

*Für Einsteiger, die in ETFs und Aktien investieren. Stand: 16.10.2026*

> **Wichtig vorab:** Die Plugins helfen dir beim **Analysieren und Lernen**. Sie geben keine Anlageberatung. Zahlen, die Claude liefert, solltest du immer an einer Originalquelle prüfen, zum Beispiel im Geschäftsbericht oder auf der Investor-Relations-Seite des Unternehmens.

---

## 1. So benutzt du die Befehle

Es gibt zwei Wege, ein Plugin zu nutzen:

| Weg | Beispiel | Erklärung |
|---|---|---|
| **Slash-Befehl** | `/model-builder:dcf-model Apple` | Du rufst den Befehl direkt auf. Der Aufbau ist immer `/plugin-name:befehl` und danach deine Angaben. |
| **Normale Sprache** | „Erstelle mir eine DCF-Bewertung für Apple“ | Claude erkennt selbst, welcher Befehl passt. Das funktioniert meistens genauso gut. |

**Tipp:** Je genauer deine Angaben sind, desto besser wird das Ergebnis. Nenne zum Beispiel Firma, Börsenkürzel (Ticker), Zeitraum und gewünschtes Format.

**Wo kommen die Daten her?** Einige Plugins sind für professionelle Datenanbieter gebaut (FactSet, Capital IQ, Daloopa). Diese Anbieter sind kostenpflichtig und bei dir **nicht verbunden**. Claude nutzt dann öffentliche Quellen wie Geschäftsberichte, SEC-Filings und das Internet. Für private Anleger reicht das meistens aus.

---

## 2. Übersicht: Welche Plugins sind installiert?

| Plugin | Wofür es gedacht ist | Nutzen für dich als Privatanleger |
|---|---|---|
| **market-researcher** | Branchen verstehen, Wettbewerber vergleichen, Ideen finden | ⭐⭐⭐ Sehr hoch |
| **earnings-reviewer** | Quartalszahlen von Unternehmen auswerten | ⭐⭐⭐ Hoch (bei Einzelaktien) |
| **model-builder** | Unternehmen bewerten (Was ist die Aktie „wert“?) | ⭐⭐ Mittel, gut zum Lernen |
| **finance** | Buchhaltung und Controlling in Unternehmen | ⭐ Gering, eher für Firmen |
| **equity-research** | Aktienanalyse wie ein Profi-Analyst: These, Termine, Erstanalyse | ⭐⭐⭐ Sehr hoch |
| **investment-banking** | Firmenverkäufe und Übernahmen (M&A) | ⭐ Gering, eher für Banker |

---

## ⭐ Dein eigener Befehl: `/aktie`

Mit diesem Befehl nennst du nur eine Aktie, und Claude nutzt die passenden Plugins nacheinander.

- **Befehl:** `/aktie SAP` oder `/aktie AAPL`
- **Was passiert:** Claude geht 9 Schritte durch: Geschäftsmodell, Branche, Wettbewerb, Finanzen der letzten 5 Jahre, letzte Quartalszahlen, Bewertungsvergleich, fairer Wert (DCF in drei Szenarien), anstehende Termine und Investment-These. Am Ende stehen eine Scorecard und ein ehrliches Fazit.
- **Ergebnis:** Bericht und Excel-Modelle landen in `Finance/Analysen/<Aktie>/`.
- **Wann sinnvoll:** Bevor du eine Einzelaktie kaufst, oder einmal im Jahr für Aktien, die du schon besitzt.
- **Die Befehlsdatei:** `Finance/.claude/commands/aktie.md`. Dort kannst du die Schritte jederzeit anpassen.
- ⚠️ Eine vollständige Analyse dauert eine Weile und verbraucht viele Tokens.
- 💡 **Lerneffekt:** Profis prüfen immer zwei Dinge getrennt, nämlich **wie gut das Unternehmen ist** und **wie teuer die Aktie ist**. Auch ein tolles Unternehmen kann ein schlechtes Investment sein, wenn du zu viel dafür bezahlst.

---

## 3. Plugin `market-researcher`: Märkte und Branchen verstehen

*Für dich am nützlichsten, weil du hier lernst, wie eine Branche funktioniert, bevor du investierst.*

### `/market-researcher:sector-overview`
- **Was es macht:** Erstellt einen Bericht über eine ganze Branche: Marktgröße, Wachstum, wichtigste Firmen, Trends und Risiken.
- **Wann sinnvoll:** Bevor du in einen **Themen-ETF** investierst (z. B. „Clean Energy“, „Halbleiter“, „Cybersecurity“) oder bevor du dir Einzelaktien einer Branche anschaust.
- **Beispiel:** `/market-researcher:sector-overview Halbleiterindustrie – einfach erklärt für Einsteiger`
- 💡 **Lerneffekt:** Ein Themen-ETF ist nur so gut wie die Branche dahinter. Wenn du die Treiber kennst, verstehst du, warum der ETF steigt oder fällt.

### `/market-researcher:competitive-analysis`
- **Was es macht:** Vergleicht Wettbewerber: Wer ist Marktführer? Wer hat welche Stärken und Schwächen? Wie unterscheiden sich die Geschäftsmodelle?
- **Wann sinnvoll:** Wenn du überlegst, eine Aktie zu kaufen, und wissen willst, ob die Firma wirklich die beste ihrer Branche ist.
- **Beispiel:** `/market-researcher:competitive-analysis Wer sind die Konkurrenten von Adidas?`
- 💡 **Lerneffekt:** Investoren sprechen vom **„Burggraben“ (Moat)**. Gemeint ist ein dauerhafter Vorteil gegenüber der Konkurrenz, zum Beispiel eine starke Marke, Patente oder Netzwerkeffekte.

### `/market-researcher:comps-analysis`
- **Was es macht:** Erstellt eine **Vergleichstabelle** mit ähnlichen Firmen und Kennzahlen wie dem KGV. Die Tabelle ist eine Excel-Datei.
- **Wann sinnvoll:** Wenn du wissen willst, ob eine Aktie im Vergleich zu ihren Konkurrenten **teuer oder günstig** ist.
- **Beispiel:** `/market-researcher:comps-analysis Vergleiche SAP mit Oracle, Microsoft und Salesforce`
- 💡 **Lerneffekt:** Das **KGV (Kurs-Gewinn-Verhältnis)** sagt dir, wie viele Jahresgewinne du für eine Aktie bezahlst. Ein KGV von 20 heißt: Du zahlst das 20-Fache des Jahresgewinns. Ein KGV ist nur **im Vergleich** aussagekräftig, denn Tech-Firmen haben fast immer ein höheres KGV als Versorger.

### `/market-researcher:idea-generation`
- **Was es macht:** Sucht nach Investmentideen anhand von Kriterien, die du vorgibst. Das nennt man ein „Screening“.
- **Wann sinnvoll:** Wenn du neue Aktien suchst, die zu deiner Strategie passen.
- **Beispiel:** `/market-researcher:idea-generation Finde europäische Dividendenaktien mit stabilem Gewinnwachstum und geringer Verschuldung`
- 💡 **Lerneffekt:** Ein Screening liefert nur **Kandidaten**, keine Kaufempfehlung. Danach musst du jedes Unternehmen einzeln prüfen.
- ⚠️ Ohne professionelle Datenanbieter ist die Suche weniger präzise als bei einem echten Aktien-Screener.

### `/market-researcher:pptx-author`
- **Was es macht:** Erstellt eine PowerPoint-Datei (.pptx).
- **Wann sinnvoll:** Wenn du eine Analyse als Präsentation haben möchtest, zum Beispiel für einen Investment-Club.

### Agent `market-researcher`
- **Was es macht:** Ein „Mitarbeiter“, der alle Schritte oben **automatisch nacheinander** ausführt: Branchenüberblick, Wettbewerb, Vergleichstabelle und Ideenliste, zusammengefasst in einem Bericht.
- **Wann sinnvoll:** Wenn du ein komplettes Dossier zu einem Thema willst.
- **Beispiel:** „Nutze den market-researcher-Agenten für eine Einführung in das Thema Künstliche Intelligenz als Investment.“

---

## 4. Plugin `earnings-reviewer`: Quartalszahlen verstehen

*Börsennotierte Firmen veröffentlichen alle drei Monate ihre Zahlen. Das nennt man **„Earnings“**. Danach schwankt der Kurs oft stark.*

### `/earnings-reviewer:earnings-preview`
- **Was es macht:** Bereitet dich **vor** den Quartalszahlen vor: Was erwarten die Analysten? Worauf solltest du achten? Wie sehen ein gutes und ein schlechtes Szenario aus?
- **Wann sinnvoll:** Ein paar Tage, bevor eine Firma aus deinem Depot ihre Zahlen veröffentlicht.
- **Beispiel:** `/earnings-reviewer:earnings-preview Was ist bei den nächsten Quartalszahlen von Nvidia wichtig?`
- 💡 **Lerneffekt:** Der Kurs reagiert nicht auf „gute“ oder „schlechte“ Zahlen. Er reagiert darauf, ob die Zahlen **besser oder schlechter als erwartet** sind. Deshalb fällt eine Aktie manchmal trotz Rekordgewinn.

### `/earnings-reviewer:earnings-analysis`
- **Was es macht:** Wertet die Zahlen **nach** der Veröffentlichung ausführlich aus: Wurden die Erwartungen übertroffen („Beat“) oder verfehlt („Miss“)? Was hat das Management angekündigt? Hat sich die Investment-These verändert? Das Ergebnis ist ein langer Bericht mit Diagrammen.
- **Wann sinnvoll:** Nachdem eine Firma aus deinem Depot berichtet hat und du verstehen willst, was die Zahlen bedeuten.
- **Beispiel:** `/earnings-reviewer:earnings-analysis Q3-Zahlen von Microsoft`
- 💡 **Lerneffekt:** Achte besonders auf die **„Guidance“**. Das ist die Prognose des Managements für die kommenden Quartale, und sie bewegt den Kurs oft stärker als die vergangenen Zahlen.

### `/earnings-reviewer:morning-note`
- **Was es macht:** Fasst kurz zusammen, was über Nacht an den Märkten passiert ist, mit Blick auf bestimmte Aktien.
- **Wann sinnvoll:** Als täglicher Überblick am Morgen für die Aktien, die dich interessieren.
- **Beispiel:** `/earnings-reviewer:morning-note Was ist über Nacht bei Apple, Tesla und dem MSCI World passiert?`

### `/earnings-reviewer:model-update`
- **Was es macht:** Aktualisiert ein bestehendes Finanzmodell (Excel) mit neuen Zahlen oder Prognosen.
- **Wann sinnvoll:** Nur wenn du schon ein eigenes Bewertungsmodell hast, zum Beispiel eines, das du mit `model-builder` erstellt hast.

### `/earnings-reviewer:audit-xls` und `/earnings-reviewer:xlsx-author`
- Siehe Abschnitt 5, sie funktionieren dort genauso.

### Agent `earnings-reviewer`
- **Was es macht:** Erledigt alles automatisch: liest Transkript und Berichte, aktualisiert das Modell und schreibt eine Analyse.
- **Wann sinnvoll:** Wenn du in der Berichtssaison mehrere Aktien auf einmal auswerten lassen willst.

---

## 5. Plugin `model-builder`: Was ist eine Aktie wert?

*Hier lernst du, wie Profis eine Aktie bewerten. Für Einsteiger anspruchsvoll, aber sehr lehrreich.*

### `/model-builder:dcf-model`
- **Was es macht:** Erstellt eine **DCF-Bewertung** (Discounted Cash Flow) als Excel-Datei. Dabei werden die zukünftigen Gewinne einer Firma geschätzt und auf heute „abgezinst“. So kommt ein fairer Wert pro Aktie heraus.
- **Wann sinnvoll:** Wenn du verstehen willst, ob der aktuelle Aktienkurs **gerechtfertigt** ist und welche Annahmen im Kurs stecken.
- **Beispiel:** `/model-builder:dcf-model Bewerte Coca-Cola und erkläre mir jeden Schritt`
- 💡 **Lerneffekt:** 100 € in 10 Jahren sind heute weniger wert als 100 € sofort, weil du das Geld heute schon anlegen könntest. Diese Idee nennt man **Abzinsen**, und sie steckt hinter jeder Unternehmensbewertung.
- ⚠️ Eine DCF reagiert sehr empfindlich auf die Annahmen. Kleine Änderungen beim Wachstum ergeben große Unterschiede im Ergebnis. Sieh das Ergebnis als Spanne, nicht als exakten Wert.

### `/model-builder:comps-analysis`
- Gleich wie bei `market-researcher`: eine Vergleichstabelle mit Kennzahlen ähnlicher Firmen.

### `/model-builder:3-statement-model`
- **Was es macht:** Füllt ein Modell mit den drei wichtigsten Finanzberichten aus und verknüpft sie:
  1. **Gewinn- und Verlustrechnung (GuV):** Wie viel hat die Firma verdient?
  2. **Bilanz:** Was besitzt die Firma, und welche Schulden hat sie?
  3. **Kapitalflussrechnung (Cashflow):** Wie viel echtes Geld ist geflossen?
- **Wann sinnvoll:** Wenn du lernen willst, wie diese drei Berichte zusammenhängen. Das braucht eine Excel-Vorlage.
- 💡 **Lerneffekt:** Ein Gewinn auf dem Papier ist nicht dasselbe wie echtes Geld. Der **Cashflow** zeigt, ob wirklich Geld reinkommt, und er lässt sich schwerer schönrechnen als der Gewinn.

### `/model-builder:lbo-model`
- **Was es macht:** Erstellt ein Modell für eine fremdfinanzierte Firmenübernahme (Leveraged Buyout).
- **Wann sinnvoll:** Für Privatanleger praktisch nie, denn das ist ein Werkzeug von Private-Equity-Firmen.

### `/model-builder:audit-xls`
- **Was es macht:** Prüft eine Excel-Datei auf Formelfehler und unlogische Werte.
- **Wann sinnvoll:** Wenn du eine eigene **Depot- oder Sparplan-Tabelle** hast und sicher sein willst, dass die Berechnungen stimmen.
- **Beispiel:** `/model-builder:audit-xls Prüfe meine Datei depot.xlsx`

### `/model-builder:xlsx-author`
- **Was es macht:** Erstellt eine fertige Excel-Datei.
- **Wann sinnvoll:** Wenn du deine Ergebnisse in Excel weiterbearbeiten willst, zum Beispiel einen ETF-Sparplan-Rechner.
- **Beispiel:** „Erstelle mir eine Excel-Tabelle, die zeigt, wie 200 € monatlich in einem ETF bei 6 % Rendite über 25 Jahre wachsen.“

### Agent `model-builder`
- Baut DCF-, LBO-, 3-Statement- oder Vergleichsmodelle komplett, ausgehend von einem Ticker und deinen Annahmen.

---

## 6. Plugin `finance`: Buchhaltung für Unternehmen

*Dieses Plugin ist für **Buchhalter und Controller in Firmen** gedacht. Für dein Depot brauchst du es kaum. Es kann dir aber helfen, Geschäftsberichte besser zu verstehen.*

| Befehl | Kurzbeschreibung | Für dich sinnvoll? |
|---|---|---|
| `/finance:financial-statements` | Erstellt GuV, Bilanz und Cashflow mit Vergleich zur Vorperiode und erklärt die Begriffe. | ✅ **Ja, zum Lernen:** „Erkläre mir die Bilanz von BASF in einfachen Worten.“ |
| `/finance:variance-analysis` | Zerlegt Abweichungen in ihre Ursachen: Warum ist der Umsatz gestiegen oder gefallen? | ✅ Teilweise: „Warum ist der Gewinn von Siemens gegenüber dem Vorjahr gesunken?“ |
| `/finance:reconciliation` | Gleicht zwei Datenquellen ab und findet Unterschiede. | 🔸 Möglich: Depotauszug mit eigener Tabelle abgleichen. |
| `/finance:journal-entry` | Erstellt Buchungssätze (Soll/Haben). | ❌ Nur für Firmen |
| `/finance:journal-entry-prep` | Bereitet Buchungen für den Monatsabschluss vor. | ❌ Nur für Firmen |
| `/finance:close-management` | Plant den Monatsabschluss einer Firma. | ❌ Nur für Firmen |
| `/finance:audit-support` | Unterstützt bei der Wirtschaftsprüfung nach SOX 404 (US-Regeln für interne Kontrollen). | ❌ Nur für Firmen |
| `/finance:sox-testing` | Testet interne Kontrollen nach SOX. | ❌ Nur für Firmen |

**Hinweis:** Das `finance`-Plugin kann auch Datenbanken und Dienste anbinden (BigQuery, Databricks, Snowflake, Gmail, Google Kalender, Slack). Für Privatanleger ist das meistens nicht nötig.

---

## 6a. Plugin `equity-research`: Analysieren wie ein Profi

*Dieses Plugin arbeitet wie ein Aktienanalyst bei einer Bank. Einige Befehle überschneiden sich mit den Plugins oben. Neu und für dich besonders wertvoll sind `thesis` und `catalysts`.*

### `/equity-research:thesis`
- **Was es macht:** Schreibt eine **Investment-These**: Warum kaufst du die Aktie, was muss passieren, damit du recht behältst, und woran merkst du, dass du falsch liegst? Die These kann später mit neuen Daten aktualisiert werden.
- **Wann sinnvoll:** **Vor jedem Kauf**, und danach regelmäßig: „Stimmt meine These für Apple noch?“
- **Beispiel:** `/equity-research:thesis Erstelle eine These für Allianz`
- 💡 **Lerneffekt:** Wer seinen Kaufgrund aufschreibt, verkauft seltener aus Panik. Du verkaufst dann, wenn die These kaputt ist, und nicht, weil der Kurs gerade fällt.

### `/equity-research:catalysts`
- **Was es macht:** Erstellt einen **Kalender mit wichtigen Terminen** für deine Aktien, zum Beispiel Quartalszahlen, Hauptversammlungen, Produktvorstellungen, Zinsentscheidungen und Gerichtsurteile.
- **Wann sinnvoll:** Damit du weißt, wann bei deinen Aktien mit großen Kursbewegungen zu rechnen ist.
- **Beispiel:** `/equity-research:catalysts Was steht in den nächsten 3 Monaten bei Apple, SAP und Novo Nordisk an?`
- 💡 **Lerneffekt:** Ein **Katalysator** ist ein Ereignis, das den Kurs in Bewegung bringt.

### `/equity-research:initiate`
- **Was es macht:** Erstellt eine **ausführliche Erstanalyse** eines Unternehmens, so wie eine Bank sie veröffentlicht, wenn sie eine Aktie neu abdeckt. Dazu gehören Recherche, Finanzmodell, Bewertung, Diagramme und ein fertiger Bericht.
- **Wann sinnvoll:** Für einen sehr tiefen Einstieg in eine Firma. Das ist noch umfangreicher als `/aktie`.

### `/equity-research:screen`
- Gleich wie `market-researcher:idea-generation`: sucht Aktien nach deinen Kriterien.

### `/equity-research:sector`
- Gleich wie `market-researcher:sector-overview`: erstellt einen Branchenüberblick.

### `/equity-research:earnings` und `/equity-research:earnings-preview`
- Gleich wie bei `earnings-reviewer`: Quartalszahlen nachher auswerten bzw. vorher vorbereiten.

### `/equity-research:morning-note` und `/equity-research:model-update`
- Gleich wie bei `earnings-reviewer`: Morgen-Überblick bzw. ein bestehendes Modell aktualisieren.

---

## 6b. Plugin `investment-banking`: Firmenübernahmen

*Dieses Plugin ist für Investmentbanker, die Firmen verkaufen oder Übernahmen planen. Für Privatanleger ist fast alles davon irrelevant.*

| Befehl | Kurzbeschreibung | Für dich sinnvoll? |
|---|---|---|
| `/investment-banking:one-pager` | Ein **Steckbrief** einer Firma auf einer Seite mit den wichtigsten Kennzahlen. | ✅ **Ja:** ein schneller Überblick über eine Aktie als Präsentation. Nutzt eigentlich eine Bank-Vorlage, ohne Vorlage fällt das Ergebnis schlichter aus. |
| `/investment-banking:merger-model` | Berechnet, ob eine Übernahme den Gewinn pro Aktie steigert oder senkt. | 🔸 Selten: wenn eine Firma aus deinem Depot eine Übernahme ankündigt. |
| `/investment-banking:cim` | Verkaufsprospekt für eine Firma, die verkauft werden soll. | ❌ Nur für Banker |
| `/investment-banking:teaser` | Anonyme Kurzbeschreibung einer Firma für Kaufinteressenten. | ❌ Nur für Banker |
| `/investment-banking:buyer-list` | Liste möglicher Käufer für eine Firma. | ❌ Nur für Banker |
| `/investment-banking:process-letter` | Regeln und Fristen für einen Bieterprozess. | ❌ Nur für Banker |
| `/investment-banking:deal-tracker` | Übersicht über laufende Deals. | ❌ Nur für Banker |

💡 **Lerneffekt:** Wenn eine Firma eine andere kauft, steigt oft die Aktie der **gekauften** Firma, weil der Käufer einen Aufschlag zahlt. Die Aktie des **Käufers** fällt dagegen häufig, weil Anleger fürchten, dass zu viel bezahlt wurde.

---

## 7. Welcher Befehl für welche Situation?

| Deine Frage | Passender Befehl |
|---|---|
| „Lohnt sich diese Aktie? Bitte alles prüfen.“ | **`/aktie <Name>`** |
| „Warum besitze ich diese Aktie eigentlich, und stimmt das noch?“ | `equity-research:thesis` |
| „Wann stehen wichtige Termine für meine Aktien an?“ | `equity-research:catalysts` |
| „Ich will in einen Themen-ETF investieren. Lohnt sich die Branche?“ | `market-researcher:sector-overview` |
| „Ist diese Aktie besser als ihre Konkurrenz?“ | `market-researcher:competitive-analysis` |
| „Ist die Aktie teuer oder günstig?“ | `market-researcher:comps-analysis` oder `model-builder:dcf-model` |
| „Ich suche neue Aktien-Ideen.“ | `market-researcher:idea-generation` |
| „Meine Aktie veröffentlicht nächste Woche Zahlen.“ | `earnings-reviewer:earnings-preview` |
| „Die Zahlen sind raus. Was bedeuten sie?“ | `earnings-reviewer:earnings-analysis` |
| „Was ist heute Nacht passiert?“ | `earnings-reviewer:morning-note` |
| „Ich verstehe den Geschäftsbericht nicht.“ | `finance:financial-statements` |
| „Stimmt meine Depot-Tabelle?“ | `model-builder:audit-xls` |
| „Ich will einen Sparplan-Rechner in Excel.“ | `model-builder:xlsx-author` |

---

## 8. Mini-Lexikon: Begriffe, die dir begegnen werden

| Begriff | Einfache Erklärung |
|---|---|
| **ETF** | Ein börsengehandelter Fonds, der einen Index nachbildet, zum Beispiel den MSCI World mit rund 1.500 Firmen. Er ist günstig und breit gestreut. |
| **Index** | Ein „Korb“ von Aktien, der einen Markt abbildet, zum Beispiel der DAX mit 40 deutschen Firmen. |
| **Ticker** | Das Börsenkürzel einer Aktie, zum Beispiel AAPL für Apple oder SAP für SAP. |
| **KGV** | Kurs-Gewinn-Verhältnis. Es sagt, wie „teuer“ eine Aktie im Verhältnis zu ihrem Gewinn ist. |
| **Dividende** | Ein Teil des Gewinns, den die Firma an ihre Aktionäre ausschüttet. |
| **Marktkapitalisierung** | Der Börsenwert einer Firma: Aktienkurs mal Anzahl der Aktien. |
| **Umsatz** | Alle Einnahmen aus Verkäufen, bevor Kosten abgezogen werden. |
| **EBIT / EBITDA** | Der Gewinn vor Zinsen und Steuern. Bei EBITDA werden zusätzlich die Abschreibungen nicht abgezogen. Damit lassen sich Firmen besser vergleichen. |
| **Free Cashflow** | Das Geld, das nach allen Ausgaben und Investitionen übrig bleibt. Es ist eine der wichtigsten Kennzahlen. |
| **Guidance** | Die Prognose des Managements für die Zukunft. |
| **Beat / Miss** | Die Zahlen sind besser bzw. schlechter als erwartet. |
| **Burggraben (Moat)** | Ein dauerhafter Wettbewerbsvorteil einer Firma. |
| **Diversifikation** | Das Risiko auf viele Anlagen verteilen („nicht alle Eier in einen Korb“). |
| **TER** | Die jährlichen Kosten eines ETFs in Prozent. Weniger ist besser. Typisch sind 0,05 % bis 0,5 %. |
| **Thesaurierend / Ausschüttend** | Ein thesaurierender ETF legt Dividenden automatisch wieder an, ein ausschüttender zahlt sie dir aus. |

---

## 9. Drei Tipps zum Schluss

1. **Klein anfangen:** Probiere zuerst `sector-overview` oder `financial-statements` mit dem Zusatz „einfach erklärt für Einsteiger“.
2. **Nachfragen:** Wenn du einen Begriff nicht verstehst, frag einfach: „Was bedeutet …?“. Claude erklärt es dir.
3. **Kritisch bleiben:** Claude kann sich bei Zahlen irren. Prüfe wichtige Werte an der Originalquelle, bevor du eine Entscheidung triffst.
