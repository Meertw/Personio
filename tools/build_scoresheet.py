"""Bouwt de Excel-scoresheet voor de Personio quickscan uit de modulebestanden.

Gebruik:
    python tools/build_scoresheet.py            # lege template
    python tools/build_scoresheet.py --voorbeeld  # ingevuld voorbeeld (fictieve klant)
"""
import glob, os, random, re, sys
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, ColorScaleRule, FormulaRule
from openpyxl.chart import BarChart, Reference

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOORBEELD = "--voorbeeld" in sys.argv
OUT = os.path.join(ROOT, "scoresheet", "quickscan-voorbeeld.xlsx" if VOORBEELD else "quickscan-template.xlsx")

F = "Arial"
H_FILL = PatternFill("solid", fgColor="1F3A5F")
H_FONT = Font(name=F, bold=True, color="FFFFFF")
IN_FILL = PatternFill("solid", fgColor="FFF7D6")
THIN = Side(style="thin", color="D0D7DE")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")


def clean(t):
    return re.sub(r"\*\*|`", "", t).strip()


def load_modules():
    mods = []
    for p in sorted(glob.glob(os.path.join(ROOT, "quickscan", "[0-9][0-9]-*.md"))):
        txt = open(p, encoding="utf-8").read()
        nr = os.path.basename(p)[:2]
        if nr == "00":
            continue
        title = clean(re.search(r"^# \d+ – (.+)$", txt, re.M).group(1))
        points = []
        for line in txt.splitlines():
            m = re.match(r"^\| (\d+\.\d+) \| (.+?) \|", line)
            if m:
                points.append((m.group(1), clean(m.group(2))))
        mods.append((nr, title, points))
    return mods


def header(ws, row, cols):
    for i, c in enumerate(cols, 1):
        cell = ws.cell(row=row, column=i, value=c)
        cell.fill, cell.font, cell.border = H_FILL, H_FONT, BORDER
        cell.alignment = Alignment(vertical="center", wrap_text=True)


def font_all(ws):
    for row in ws.iter_rows():
        for c in row:
            if c.font is None or c.font.name != F:
                c.font = Font(name=F, bold=c.font.bold, color=c.font.color, size=c.font.size, italic=c.font.italic)


# ---------- voorbeelddata (fictief) ----------
random.seed(7)
VB_SCORES = {"01": 1, "02": 0, "03": 2, "04": 1, "05": 2, "06": 1, "07": 2, "08": 2,
             "09": 1, "10": 1, "11": 1, "12": 0, "13": 2, "14": 1, "15": 0}
VB_FINDINGS = {
    "1.1": ("Er zijn 22 job families; veel overlap (bijv. 'Sales' en 'Commercie').", "Terugbrengen naar 9 families.", "Hoog"),
    "1.6": ("148 unieke functietitels bij 210 medewerkers.", "Titels standaardiseren o.b.v. job catalog.", "Hoog"),
    "2.5": ("Vacatures worden per mail goedgekeurd door de directeur.", "Planning Cycles met approval chain inrichten.", "Hoog"),
    "4.6": ("Afwijzingsmails worden handmatig per kandidaat verstuurd.", "Templates per fase + bulkmail.", "Middel"),
    "4.11": ("Geen agendakoppeling; recruiter mailt over beschikbaarheid.", "Cronofy-koppeling met Office 365 inrichten.", "Middel"),
    "4.15": ("AI Signals niet in gebruik.", "Pilot met 2 vacatures; profiel opstellen met hiring manager.", "Laag"),
    "6.3": ("Medewerkers kunnen IBAN direct wijzigen zonder goedkeuring.", "Recht op Propose zetten + approval door HR.", "Hoog"),
    "7.9": ("Frequent verzuim wordt niet gesignaleerd.", "Workflow op ziekmelding met signaal naar HR.", "Middel"),
    "9.6": ("Geen herinneringen als onboardingtaken over de deadline gaan.", "Herinneringen + escalatie naar HR instellen.", "Middel"),
    "12.2": ("Geen salarisbanden in Personio.", "Banden per family/level inrichten (voorbereiding loontransparantie).", "Hoog"),
    "13.2": ("Voorlopige payroll wordt niet altijd goedgekeurd vóór export.", "Checklist maandafsluiting invoeren.", "Hoog"),
    "15.2": ("Handboek staat op SharePoint, niet gekoppeld.", "Handboek koppelen aan de Assistant.", "Laag"),
}


def build():
    mods = load_modules()
    wb = Workbook()

    # ---------- Instructie ----------
    ws = wb.active
    ws.title = "Instructie"
    ws["A1"] = "Personio Quickscan – scoresheet"
    ws["A1"].font = Font(name=F, bold=True, size=16, color="1F3A5F")
    lines = [
        ("Klant", "Voorbeeld BV (fictief)" if VOORBEELD else ""),
        ("Datum scan", "2026-11-03" if VOORBEELD else ""),
        ("Consultant", "worldofwork" if VOORBEELD else ""),
        ("", ""),
        ("Zo werkt het", ""),
        ("1.", "Vul tabblad 'Intake' in (vooraf of in de eerste sessie)."),
        ("2.", "Loop per module de controlepunten door op tabblad 'Controlepunten'."),
        ("3.", "Vul alleen de gele cellen in: Score (0-3), Bevinding, Advies en Prio (Hoog/Middel/Laag)."),
        ("4.", "Laat de score leeg als een punt niet van toepassing is; het telt dan niet mee."),
        ("5.", "Het tabblad 'Dashboard' en 'Actielijst' worden automatisch bijgewerkt."),
        ("", ""),
        ("Score", "0 = ontbreekt · 1 = basis · 2 = goed · 3 = geoptimaliseerd"),
        ("Prio", "Hoog = blokkeert of risico · Middel = kost tijd / onbetrouwbare data · Laag = verbetering"),
        ("Bron", "Controlepunten komen uit de modules in de repository Meertw/Personio (map quickscan/)."),
    ]
    for i, (a, b) in enumerate(lines, 3):
        ws.cell(row=i, column=1, value=a).font = Font(name=F, bold=True)
        c = ws.cell(row=i, column=2, value=b)
        if i <= 5:
            c.fill = IN_FILL
    ws.column_dimensions["A"].width = 16
    ws.column_dimensions["B"].width = 95

    # ---------- Intake ----------
    wi = wb.create_sheet("Intake")
    header(wi, 1, ["Onderwerp", "Antwoord klant"])
    intake = re.findall(r"^\| (?!Onderwerp|-)(.+?) \| \|$",
                        open(os.path.join(ROOT, "quickscan", "00-intake.md"), encoding="utf-8").read(), re.M)
    vb_intake = ["Voorbeeld BV", "210 / 280", "2 (NL, BE)", "2023", "Core Pro + Recruiting + Performance",
                 "Nmbrs, via koppeling", "Microsoft 365 (SSO), Teams", "1 HR-beheerder (0,6 fte)",
                 "Veel handwerk in recruiting; geen inzicht in salarisopbouw", "Loontransparantie, minder handwerk",
                 "HR-manager, 2026-11-03"]
    for i, q in enumerate(intake, 2):
        wi.cell(row=i, column=1, value=q).border = BORDER
        c = wi.cell(row=i, column=2, value=vb_intake[i - 2] if VOORBEELD and i - 2 < len(vb_intake) else None)
        c.fill, c.border = IN_FILL, BORDER
    wi.column_dimensions["A"].width = 45
    wi.column_dimensions["B"].width = 70

    # ---------- Controlepunten ----------
    wc = wb.create_sheet("Controlepunten")
    cols = ["Module", "Modulenaam", "#", "Controlepunt", "Score (0-3)", "Bevinding", "Advies", "Prio"]
    header(wc, 1, cols)
    r = 2
    for nr, title, points in mods:
        for pid, text in points:
            vals = [nr, title, pid, text]
            for ci, v in enumerate(vals, 1):
                c = wc.cell(row=r, column=ci, value=v)
                c.border, c.alignment = BORDER, WRAP
            for ci in range(5, 9):
                c = wc.cell(row=r, column=ci)
                c.fill, c.border, c.alignment = IN_FILL, BORDER, WRAP
            if VOORBEELD:
                base = VB_SCORES[nr]
                wc.cell(row=r, column=5, value=max(0, min(3, base + random.choice([-1, 0, 0, 1]))))
                if pid in VB_FINDINGS:
                    f, a, p = VB_FINDINGS[pid]
                    wc.cell(row=r, column=5, value=0 if p == "Hoog" else 1)
                    wc.cell(row=r, column=6, value=f)
                    wc.cell(row=r, column=7, value=a)
                    wc.cell(row=r, column=8, value=p)
            r += 1
    last = r - 1
    for col, w in zip("ABCDEFGH", [8, 26, 7, 70, 10, 40, 40, 10]):
        wc.column_dimensions[col].width = w
    wc.freeze_panes = "E2"
    wc.auto_filter.ref = f"A1:H{last}"
    dv_s = DataValidation(type="whole", operator="between", formula1="0", formula2="3", allow_blank=True,
                          error="Vul 0, 1, 2 of 3 in.", showErrorMessage=True)
    dv_p = DataValidation(type="list", formula1='"Hoog,Middel,Laag"', allow_blank=True)
    wc.add_data_validation(dv_s); wc.add_data_validation(dv_p)
    dv_s.add(f"E2:E{last}"); dv_p.add(f"H2:H{last}")
    wc.conditional_formatting.add(f"E2:E{last}", CellIsRule(operator="equal", formula=["0"], fill=PatternFill("solid", fgColor="F8D7DA")))
    wc.conditional_formatting.add(f"E2:E{last}", CellIsRule(operator="equal", formula=["1"], fill=PatternFill("solid", fgColor="FCE8C8")))
    wc.conditional_formatting.add(f"E2:E{last}", CellIsRule(operator="equal", formula=["2"], fill=PatternFill("solid", fgColor="DDF0DD")))
    wc.conditional_formatting.add(f"E2:E{last}", CellIsRule(operator="equal", formula=["3"], fill=PatternFill("solid", fgColor="B7E1B7")))
    wc.conditional_formatting.add(f"H2:H{last}", CellIsRule(operator="equal", formula=['"Hoog"'], font=Font(name=F, bold=True, color="B00020")))

    # ---------- Dashboard ----------
    wd = wb.create_sheet("Dashboard", 1)
    wd["A1"] = "Dashboard – resultaat per module"
    wd["A1"].font = Font(name=F, bold=True, size=14, color="1F3A5F")
    wd["A2"] = "Automatisch berekend uit tabblad 'Controlepunten'. Gemiddelde score 0-3; lege scores tellen niet mee."
    wd["A2"].font = Font(name=F, italic=True, color="555555")
    header(wd, 4, ["Module", "Modulenaam", "Aantal punten", "Gescoord", "Gem. score", "Volwassenheid %", "Prio Hoog", "Status"])
    rng = lambda col: f"Controlepunten!${col}$2:${col}${last}"
    for i, (nr, title, points) in enumerate(mods, 5):
        wd.cell(row=i, column=1, value=nr)
        wd.cell(row=i, column=2, value=title)
        wd.cell(row=i, column=3, value=f'=COUNTIF({rng("A")},A{i})')
        wd.cell(row=i, column=4, value=f'=COUNTIFS({rng("A")},A{i},{rng("E")},"<>")')
        wd.cell(row=i, column=5, value=f'=IF(D{i}=0,"",AVERAGEIFS({rng("E")},{rng("A")},A{i}))')
        wd.cell(row=i, column=6, value=f'=IF(E{i}="","",E{i}/3)')
        wd.cell(row=i, column=7, value=f'=COUNTIFS({rng("A")},A{i},{rng("H")},"Hoog")')
        wd.cell(row=i, column=8, value=f'=IF(E{i}="","Niet gescoord",IF(E{i}<1,"Ontbreekt",IF(E{i}<2,"Basis",IF(E{i}<2.5,"Goed","Geoptimaliseerd"))))')
        for ci in range(1, 9):
            wd.cell(row=i, column=ci).border = BORDER
        wd.cell(row=i, column=5).number_format = "0.0"
        wd.cell(row=i, column=6).number_format = "0%"
    end = 4 + len(mods)
    t = end + 1
    wd.cell(row=t, column=2, value="Totaal").font = Font(name=F, bold=True)
    wd.cell(row=t, column=3, value=f"=SUM(C5:C{end})")
    wd.cell(row=t, column=4, value=f"=SUM(D5:D{end})")
    wd.cell(row=t, column=5, value=f'=IF(D{t}=0,"",AVERAGE({rng("E")}))').number_format = "0.0"
    wd.cell(row=t, column=6, value=f'=IF(E{t}="","",E{t}/3)').number_format = "0%"
    wd.cell(row=t, column=7, value=f"=SUM(G5:G{end})")
    for ci in range(1, 9):
        c = wd.cell(row=t, column=ci); c.border = BORDER; c.font = Font(name=F, bold=True)
    wd.conditional_formatting.add(f"F5:F{end}", ColorScaleRule(start_type="num", start_value=0, start_color="F8D7DA",
                                                                 mid_type="num", mid_value=0.5, mid_color="FCE8C8",
                                                                 end_type="num", end_value=1, end_color="B7E1B7"))
    for col, w in zip("ABCDEFGH", [8, 40, 13, 11, 11, 15, 10, 16]):
        wd.column_dimensions[col].width = w
    ch = BarChart(); ch.type = "bar"; ch.style = 10
    ch.title = "Gemiddelde score per module (0-3)"; ch.legend = None
    ch.add_data(Reference(wd, min_col=5, min_row=4, max_row=end), titles_from_data=True)
    ch.set_categories(Reference(wd, min_col=2, min_row=5, max_row=end))
    ch.y_axis.scaling.min = 0; ch.y_axis.scaling.max = 3; ch.y_axis.majorUnit = 1
    ch.x_axis.scaling.orientation = "maxMin"
    ch.height, ch.width = 10, 18
    wd.add_chart(ch, "J4")

    # ---------- Actielijst ----------
    wa = wb.create_sheet("Actielijst", 2)
    wa["A1"] = "Actielijst – alle bevindingen met prioriteit"
    wa["A1"].font = Font(name=F, bold=True, size=14, color="1F3A5F")
    wa["A2"] = "Automatisch: toont regels uit 'Controlepunten' met een prioriteit, gesorteerd Hoog → Middel → Laag."
    wa["A2"].font = Font(name=F, italic=True, color="555555")
    header(wa, 4, ["Prio", "#", "Module", "Controlepunt", "Bevinding", "Advies", "Score"])
    # hulpkolom in Controlepunten (I): sorteersleutel
    wc.cell(row=1, column=9, value="Sorteer (hulp)").font = Font(name=F, color="999999")
    for rr in range(2, last + 1):
        wc.cell(row=rr, column=9, value=f'=IF(H{rr}="Hoog",1,IF(H{rr}="Middel",2,IF(H{rr}="Laag",3,0)))*10000+IF(H{rr}="",0,ROW())')
        wc.cell(row=rr, column=9).font = Font(name=F, color="999999")
    wc.column_dimensions["I"].hidden = True
    n_rows = 60
    for k in range(1, n_rows + 1):
        rr = 4 + k
        key = f'IF(COUNTIF(Controlepunten!$I$2:$I${last},">0")<{k},0,SMALL(Controlepunten!$I$2:$I${last},COUNTIF(Controlepunten!$I$2:$I${last},0)+{k}))'
        wa.cell(row=rr, column=8, value=f"={key}").font = Font(name=F, color="999999")
        for ci, col in zip(range(1, 8), ["H", "C", "B", "D", "F", "G", "E"]):
            wa.cell(row=rr, column=ci, value=f'=IF($H{rr}=0,"",INDEX(Controlepunten!${col}$2:${col}${last},MOD($H{rr},10000)-1))')
            wa.cell(row=rr, column=ci).border = BORDER
            wa.cell(row=rr, column=ci).alignment = WRAP
    wa.column_dimensions["H"].hidden = True
    for col, w in zip("ABCDEFG", [9, 7, 26, 55, 45, 45, 8]):
        wa.column_dimensions[col].width = w
    wa.conditional_formatting.add(f"A5:A{4+n_rows}", CellIsRule(operator="equal", formula=['"Hoog"'], font=Font(name=F, bold=True, color="B00020")))

    for s in wb.worksheets:
        font_all(s)
    for s, cell in [(ws, "A1"), (wd, "A1"), (wa, "A1")]:
        s[cell].font = Font(name=F, bold=True, size=16 if s is ws else 14, color="1F3A5F")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    wb.save(OUT)
    print(OUT, "rows:", last - 1)


if __name__ == "__main__":
    build()
