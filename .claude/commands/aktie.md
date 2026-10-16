---
description: Vollständige Aktienanalyse für Einsteiger (alle Finanz-Plugins)
argument-hint: <Aktienname oder Ticker, z. B. SAP oder AAPL>
---

Analysiere die Aktie **$ARGUMENTS** vollständig für mich. Ich bin Privatanleger
und Einsteiger und investiere langfristig in ETFs und Einzelaktien. Antworte auf
Deutsch und erkläre jeden Fachbegriff beim ersten Auftreten in einem Satz.

Falls "$ARGUMENTS" leer oder mehrdeutig ist (z. B. mehrere Aktiengattungen oder
Börsenplätze), frage zuerst nach, welche Aktie gemeint ist.

Arbeite diese Schritte nacheinander ab und nutze die passenden Plugins:

1. **Unternehmen & Geschäftsmodell:** Womit verdient die Firma ihr Geld? Welche
   Segmente und Regionen gibt es? (equity-research:initiating-coverage, Teil 1)
2. **Branche:** Wie groß ist der Markt, wie stark wächst er, welche Trends und
   Risiken gibt es? (market-researcher:sector-overview, Kurzfassung)
3. **Wettbewerb:** Wer sind die 3–5 wichtigsten Konkurrenten? Hat die Firma einen
   dauerhaften Wettbewerbsvorteil (Burggraben)? (market-researcher:competitive-analysis)
4. **Finanzen der letzten 5 Jahre:** Umsatz, Gewinn, Marge, Free Cashflow,
   Verschuldung, Dividende. Trends verständlich erklären. (finance:financial-statements)
5. **Letzte Quartalszahlen:** Erwartungen übertroffen oder verfehlt? Was sagt die
   Guidance? (earnings-reviewer:earnings-analysis, Kurzfassung)
6. **Bewertung im Vergleich:** KGV, EV/EBITDA, Dividendenrendite gegenüber den
   Konkurrenten. (model-builder:comps-analysis)
7. **Fairer Wert:** DCF-Bewertung mit drei Szenarien (pessimistisch, realistisch,
   optimistisch) und Vergleich zum aktuellen Kurs. (model-builder:dcf-model)
8. **Anstehende Termine:** Quartalszahlen, Hauptversammlung, Produktstarts und
   andere Ereignisse, die den Kurs bewegen können. (equity-research:catalysts)
9. **Investment-These:** 3 Gründe dafür, 3 Gründe dagegen, die größten Risiken und
   woran ich merke, dass die These nicht mehr stimmt. (equity-research:thesis)

Zum Schluss:
- Eine **Scorecard** (1–5 Punkte) für Geschäftsmodell, Wachstum, Finanzkraft,
  Bewertung und Risiko, jeweils mit kurzer Begründung.
- Ein **ehrliches Fazit:** Ist die Aktie aktuell eher günstig, fair oder teuer?
  Für welchen Anlegertyp passt sie? Was bringt sie mir zusätzlich zu einem breiten
  ETF wie dem MSCI World, den ich vielleicht schon habe?
- Die **3 wichtigsten Dinge**, die ich aus dieser Analyse lernen kann.
- **Datenstand und Quellen**; markiere unsichere oder geschätzte Zahlen.
- Hinweis: Dies ist keine Anlageberatung.

Speichere den Bericht als `Bericht.md` und die Bewertungsmodelle als Excel unter
`/home/user/Finance/Analysen/<Name der Aktie>/`.
