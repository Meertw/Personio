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
| 5.7 | Eigen attributen zijn per entiteit zichtbaar gemaakt waar dat nodig is (bijv. een veld dat alleen voor de NL-entiteit of één bv geldt), zodat medewerkers van andere entiteiten geen irrelevante velden zien (let op: dit regelt alleen de weergave, niet de rechten – zie module 06) | | | | |
| 5.8 | Er is een eigenaar en een proces voor het toevoegen of aanpassen van attributen | | | | |
| 5.9 | De IBAN-validatie in het profiel wordt gebruikt en ongeldige IBAN's worden opgelost | | | | |
| 5.10 | Attributen die naar payroll of andere systemen gaan, sluiten aan op de integratie (module 13) | | | | |

## Datacheck

- [ ] Export alle medewerkers met alle attributen: percentage gevuld per attribuut
- [ ] Attributen die bij niemand of bijna niemand gevuld zijn (kandidaat om te verwijderen)
- [ ] Vrije-tekstvelden met veel varianten (kandidaat voor keuzelijst)
- [ ] Eigen attributen per entiteit: is elk veld relevant voor alle entiteiten waar het zichtbaar is?
- [ ] Gegevens die buiten Personio in Excel worden bijgehouden voor rapportage (kandidaat voor eigen attribuut)

## Veelvoorkomende hiaten

- Rapportagegegevens (bijv. uren ouderschapsverlof) staan in een losse Excel in plaats van in een attribuut
- Alle eigen velden zijn voor alle entiteiten zichtbaar, ook als ze maar voor één entiteit gelden
- Te veel ongebruikte velden, waardoor het profiel onoverzichtelijk wordt
- Vrije tekst waar een keuzelijst hoort, waardoor rapportages niet kloppen

## Praktijktips

- Wil je iets meenemen voor **rapportagedoeleinden**, bijvoorbeeld **uren ouderschapsverlof** voor analytics? **Voeg het toe als attribuut** en haal het daarna op in **Reporting**.
- **Eigen attributen** kun je **per entiteit zichtbaar** maken. Handig als een klant meerdere entiteiten of landen heeft, met verschillende velden per entiteit (bijv. land-specifieke payrollgegevens).

## Antwoorden van Personio

_Bron: schriftelijke antwoorden van Personio na de demosessie (oktober 2026)._

- **IBAN-validatie**: Personio controleert in het medewerkersprofiel of een IBAN geldig is, markeert ongeldige invoer en helpt met de opmaak.
- **Let op**: payrollproviders (bijv. Nmbrs) kunnen eigen validatieregels hebben. Een IBAN die Personio accepteert, wordt dus niet altijd door de payrollkoppeling geaccepteerd (zie module 13).

## Tips uit Personio Help

_Bron: Personio Help Center en Personio Community (stand oktober 2026). (C) = community-bericht, geen officiële documentatie. Controleer menupaden in de eigen omgeving van de klant._

- Attribuuttypes: tekst (max. 2.000 tekens), meerregelige tekst, link, datum (met herinneringen), getal (2 decimalen), keuzelijst, meerkeuze en tags. **Het type kun je achteraf niet wijzigen** – kies vooraf goed. Optie **'must be unique'** bijv. voor personeelsnummer. ([bron](https://support.personio.de/hc/en-us/articles/208861829))
- Wijzigingen kunnen **direct, met terugwerkende kracht of gepland** worden doorgevoerd (geplande wijziging om 03:00 op de gekozen datum). Met **'Set as temporary change'** zet je een waarde later automatisch terug. Advies: de startdatum niet met terugwerkende kracht wijzigen. ([bron](https://support.personio.de/hc/en-us/articles/213331029))
- **Attributen per juridische entiteit** veranderen alleen de **weergave** van het profiel, **niet de rechten**: de attributen blijven zichtbaar in rapportages en de People List. Combineer daarom met rechten (module 06). ([bron](https://support.personio.de/hc/en-us/articles/115002699585))
- (C) De Employee API geeft **geen attribuuthistorie** terug – relevant voor koppelingen en datachecks via API. ([bron](https://community.personio.com/employee-data-documents-86/employee-api-retro-active-changes-not-available-5486))
- Medewerkers importeren via **Settings > Organization > Imports**; de import faalt als je geen edit-rechten hebt op een van de kolommen. ([bron](https://support.personio.de/hc/en-us/articles/115002699585))

## Opleverpunten voor de klant

- Attributenoverzicht: behouden / aanpassen / verwijderen / toevoegen
- Voorstel voor eigen attributen ten behoeve van rapportage en analytics
- Overzicht welke eigen attributen voor welke entiteit zichtbaar zijn
