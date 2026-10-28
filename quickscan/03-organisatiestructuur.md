# 03 – Organisatiestructuur

> **Waarom belangrijk?** Entiteiten, vestigingen (offices), afdelingen, teams en kostenplaatsen zijn de basis voor planning (module 02), verlofregelingen (module 07), rechten (module 06), payroll (module 13) en rapportages (module 14).

## Begrippen

- **Juridische entiteit (legal entity)** – de werkgever op papier; wordt via een attribuut aan de medewerker gekoppeld.
- **Vestiging (office / workplace)** – een fysieke locatie met eigen adres, valuta, tijdzone en eventueel feestdagenkalender.
- **Afdeling** – de verplichte hoofdstructuur, met eventueel subafdelingen.
- **Team** – optioneel, voor matrix- of afdelingsoverstijgende samenwerking.
- **Kostenplaats** – voor de verdeling van loonkosten.

## Controlepunten

| # | Controlepunt | Score (0-3) | Bevinding | Advies | Prio |
|---|--------------|-------------|-----------|--------|------|
| 3.1 | Alle juridische entiteiten zijn aangemaakt en iedere medewerker is aan de juiste entiteit gekoppeld | | | | |
| 3.2 | Iedere fysieke locatie is een aparte vestiging met adres, tijdzone en de juiste feestdagenkalender | | | | |
| 3.3 | De afdelingsstructuur (incl. subafdelingen) komt overeen met het organogram | | | | |
| 3.4 | Teams worden alleen gebruikt waar dat iets toevoegt (matrix / projecten), niet als dubbeling van afdelingen | | | | |
| 3.5 | Iedere medewerker heeft een primaire leidinggevende (nodig voor rechten op 'Reporting line' en goedkeuringen) | | | | |
| 3.6 | Kostenplaatsen zijn ingericht en sluiten aan op finance en payroll | | | | |
| 3.7 | Er is een eigenaar en een proces voor wijzigingen in de structuur (reorganisatie, nieuwe vestiging) | | | | |

## Datacheck

- [ ] Medewerkers zonder entiteit, vestiging, afdeling of leidinggevende
- [ ] Lege of dubbele afdelingen/teams
- [ ] Kostenplaatsverdeling per medewerker (telt op tot 100%?)

## Veelvoorkomende hiaten

- Afdelingen en teams door elkaar gebruikt
- Vestigingen zonder feestdagenkalender, waardoor verlofsaldi niet kloppen
- Medewerkers zonder leidinggevende, waardoor goedkeuringen vastlopen

## Tips uit Personio Help

_Bron: Personio Help Center en Personio Community (stand oktober 2026). (C) = community-bericht, geen officiële documentatie._

- Aanbevolen volgorde: eerst bedrijfsgegevens, dan **vestigingen en juridische entiteiten**, daarna **afdelingen en teams**. ([bron](https://support.personio.de/hc/en-us/articles/21495336264733))
- Elke fysieke locatie is een eigen vestiging met adres, valuta, tijdzone en optioneel een feestdagenkalender; **geofencing** voor tijdregistratie kun je per vestiging aanzetten. ([bron](https://support.personio.de/hc/en-us/articles/209388769))
- **Afdelingen** zijn de verplichte hoofdstructuur met subafdelingen; **teams** zijn optioneel (met subteams) en bedoeld voor matrix- of afdelingsoverstijgende samenwerking. ([bron](https://support.personio.de/hc/en-us/articles/18862110441885))
- (C) Het standaard kostenplaatsattribuut ondersteunt **meerdere kostenplaatsen met een procentuele verdeling**. ([bron](https://community.personio.com/grupo-espanol-de-rr-hh-91/cost-centers-1205))
- Let op bij koppelingen: de DATEV-integratie neemt alleen de **primaire** kostenplaats mee, niet de verdeling – controleer dit ook voor de eigen payrollkoppeling. ([bron](https://support.personio.de/hc/en-us/articles/37157446396317))

## Praktijktips

_Wordt aangevuld vanuit [`tips/tips-log.md`](../tips/tips-log.md)._

## Opleverpunten voor de klant

- Overzicht structuur: entiteiten, vestigingen, afdelingen, teams, kostenplaatsen
- Opschoonlijst (ontbrekende koppelingen, dubbelingen)
