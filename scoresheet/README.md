# Scoresheet

| Bestand | Gebruik |
|---------|---------|
| `quickscan-template.xlsx` | Lege scoresheet voor een klant |
| `quickscan-voorbeeld.xlsx` | Ingevuld voorbeeld met een fictieve klant (Voorbeeld BV) |

**Tabbladen:** Instructie · Dashboard (score per module + grafiek) · Actielijst (bevindingen gesorteerd op prio) · Intake · Controlepunten (vul de gele cellen in).

**Opnieuw genereren** na wijzigingen in de modules:

```bash
python tools/build_scoresheet.py              # template
python tools/build_scoresheet.py --voorbeeld  # voorbeeld
```

De controlepunten worden automatisch uit `quickscan/*.md` gehaald. Open het bestand daarna één keer in Excel (of LibreOffice) zodat de formules worden berekend.
