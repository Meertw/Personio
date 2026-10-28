# 05 – Medewerkersattributen & datakwaliteit

> **Waarom belangrijk?** Attributen zijn de velden in het medewerkersprofiel. Wat hier niet goed staat, komt niet goed terug in workflows, payroll en rapportages. Je kunt ook **eigen attributen** toevoegen, specifiek voor rapportage- en analysedoeleinden.

## Begrippen

- **Standaardattribuut** – een veld dat Personio standaard heeft (bijv. naam, afdeling, functie, startdatum).
- **Eigen (custom) attribuut** – een veld dat de klant zelf toevoegt, bijv. *uren ouderschapsverlof*.
- **Attribuutsectie** – een groep attributen in het profiel (bijv. Persoonlijk, Contract, Salaris).

## Controlepunten

| # | Controlepunt | Score (0-3) | Bevinding | Advies | Prio |
|---|--------------|-------------|-----------|--------|------|
| 5.1 | Attributen zijn logisch gegroepeerd in secties en er staan geen ongebruikte of dubbele velden | | | | |
| 5.2 | Het juiste veldtype wordt gebruikt (keuzelijst/datum/getal in plaats van vrije tekst waar mogelijk) | | | | |
| 5.3 | Verplichte velden zijn bepaald (wat moet altijd gevuld zijn voor payroll, rapportage en workflows) | | | | |
| 5.4 | Waar wijzigingen in de tijd belangrijk zijn (functie, salaris, uren) wordt historie bijgehouden met ingangsdatum | | | | |
| 5.5 | Er zijn eigen attributen toegevoegd voor rapportage- en analysedoelen (bijv. uren ouderschapsverlof) | | | | |
| 5.6 | Deze eigen attributen zijn ook echt op te halen en worden gebruikt in Reporting / Analytics | | | | |
| 5.7 | Er is een eigenaar en een proces voor het toevoegen of aanpassen van attributen | | | | |
| 5.8 | Attributen die naar payroll of andere systemen gaan, sluiten aan op de integratie (module 13) | | | | |

## Datacheck

- [ ] Export alle medewerkers met alle attributen: percentage gevuld per attribuut
- [ ] Attributen die bij niemand of bijna niemand gevuld zijn (kandidaat om te verwijderen)
- [ ] Vrije-tekstvelden met veel varianten (kandidaat voor keuzelijst)
- [ ] Gegevens die buiten Personio in Excel worden bijgehouden voor rapportage (kandidaat voor eigen attribuut)

## Veelvoorkomende hiaten

- Rapportagegegevens (bijv. uren ouderschapsverlof) staan in een losse Excel in plaats van in een attribuut
- Te veel ongebruikte velden, waardoor het profiel onoverzichtelijk wordt
- Vrije tekst waar een keuzelijst hoort, waardoor rapportages niet kloppen

## Praktijktips

- Wil je iets meenemen voor **rapportagedoeleinden**, bijvoorbeeld **uren ouderschapsverlof** voor analytics? **Voeg het toe als attribuut** en haal het daarna op in **Reporting**.

## Opleverpunten voor de klant

- Attributenoverzicht: behouden / aanpassen / verwijderen / toevoegen
- Voorstel voor eigen attributen ten behoeve van rapportage en analytics
