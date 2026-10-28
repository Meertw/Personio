# 06 – Rollen & rechten

> **Waarom belangrijk?** In Personio kun je rollen en rechten **echt per attribuut** instellen. Daarmee bepaal je precies wie wat mag zien, wijzigen of voorstellen. Dit is belangrijk voor privacy (AVG) en voor de datakwaliteit.

## Begrippen

- **Rol** – een set rechten die aan een groep gebruikers wordt toegekend (bijv. Medewerker, Manager, HR, Recruiter, Hiring manager, Finance).
- **Recht per attribuut** – per veld instellen of een rol het mag **zien**, **wijzigen** of een **wijziging voorstellen**.
- **Wijziging voorstellen** – de medewerker past een gegeven niet direct aan maar stelt een wijziging voor, die HR (of een andere goedkeurder) eerst goedkeurt.

## Controlepunten

| # | Controlepunt | Score (0-3) | Bevinding | Advies | Prio |
|---|--------------|-------------|-----------|--------|------|
| 6.1 | Er is een vastgestelde set rollen die aansluit op de organisatie (niet per persoon losse rechten) | | | | |
| 6.2 | Rechten zijn per attribuut ingesteld (zien / wijzigen / voorstellen) in plaats van alles-of-niets | | | | |
| 6.3 | Medewerkers kunnen gevoelige of payroll-relevante gegevens (bijv. IBAN, adres, burgerlijke staat) niet zelf direct wijzigen, maar alleen een wijziging voorstellen | | | | |
| 6.4 | Voorgestelde wijzigingen worden goedgekeurd door de juiste persoon en op tijd verwerkt | | | | |
| 6.5 | Waar medewerkers niets mogen aanpassen, is wijzigen volledig afgeschermd | | | | |
| 6.6 | Managers zien alleen de gegevens van hun eigen team, en alleen de attributen die zij nodig hebben | | | | |
| 6.7 | Gevoelige gegevens (salaris, verzuim, BSN) zijn alleen zichtbaar voor rollen die ze nodig hebben | | | | |
| 6.8 | Recruiting-rollen (recruiter, hiring manager) zijn apart ingericht (zie module 04) | | | | |
| 6.9 | Rollen en rechten worden periodiek gecontroleerd (bijv. bij functiewijziging of uit dienst) | | | | |

## Datacheck

- [ ] Overzicht van rollen en aantal gebruikers per rol
- [ ] Gebruikers met beheerdersrechten (zo weinig mogelijk)
- [ ] Per gevoelig attribuut: welke rollen kunnen zien / wijzigen / voorstellen
- [ ] Openstaande voorgestelde wijzigingen en hoe lang ze al openstaan

## Veelvoorkomende hiaten

- Medewerkers kunnen alles zelf wijzigen, ook payroll-gegevens, zonder controle
- Of juist: medewerkers kunnen niets doorgeven, waardoor HR alle wijzigingen met de hand doet
- Te veel beheerders
- Managers zien meer dan nodig (bijv. salaris of verzuimredenen)

## Praktijktips

- Je kunt **medewerkers beperken** in het **bijwerken van informatie** en in plaats daarvan laten werken met **wijzigingen voorstellen**.
- **Rollen en rechten** kun je **echt per attribuut** aanpassen.

## Tips uit Personio Help

_Bron: Personio Help Center en Personio Community (stand oktober 2026). (C) = community-bericht, geen officiële documentatie. Controleer menupaden in de eigen omgeving van de klant._

- Per sectie zijn er drie toegangsniveaus: **View**, **Propose** (wijziging gaat via goedkeuring) en **Edit** (direct, zonder goedkeuring). **Let op:** als er geen goedkeuringsproces aan Propose hangt, wordt de wijziging direct opgeslagen. ([bron](https://support.personio.de/hc/en-us/articles/36539231813661))
- Per recht stel je een **scope** in, zoals **Own** (eigen profiel) of **Reporting line** (op basis van de primaire leidinggevende, standaard inclusief indirecte medewerkers). Personio waarschuwt bij toegang tot gevoelige data. ([bron](https://support.personio.de/hc/en-us/articles/29339334542109))
- Alleen **Administrators** kunnen rollen en rechten instellen – houd het aantal admins klein. ([bron](https://support.personio.de/hc/en-us/articles/115005971085))
- Goedkeuringen voor voorgestelde wijzigingen richt je in onder **Automations > Workflows > Approvals**, met leidinggevenden of rollen als goedkeurder. ([bron](https://support.personio.de/hc/en-us/articles/360000905085))

## Opleverpunten voor de klant

- Rollen- en rechtenmatrix: rol × attribuut (zien / wijzigen / voorstellen)
- Advies welke attributen medewerkers zelf mogen wijzigen, alleen mogen voorstellen of niet mogen aanpassen
