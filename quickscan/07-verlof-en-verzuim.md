# 07 – Verlof & verzuim (Time off)

> **Waarom belangrijk?** Verlofregels verschillen vaak per entiteit (land, cao, contract). In Personio koppel je **verlofregelingen (leave policies) op basis van de entiteit**. Voor verzuim kun je een **workflow** maken die ziekmeldingen **signaleert** en helpt om **patronen** te herkennen.

## Begrippen

- **Leave policy / verlofregeling** – de regels voor een verloftype: opbouw, saldo, meenemen naar volgend jaar, vervaldatum, goedkeuring.
- **Verloftype (absence type)** – bijv. vakantie, bijzonder verlof, ouderschapsverlof, ziekte.
- **Toewijzing op entiteit** – medewerkers krijgen automatisch de juiste regeling op basis van hun entiteit.
- **Verzuimpatroon** – terugkerend verzuim, bijv. vaak kort ziek of steeds op maandag/vrijdag.

## Controlepunten

### Verlof

| # | Controlepunt | Score (0-3) | Bevinding | Advies | Prio |
|---|--------------|-------------|-----------|--------|------|
| 7.1 | Verlofregelingen zijn per entiteit ingericht en iedere medewerker heeft de regeling van zijn/haar entiteit; er is een vaste werkwijze voor toewijzing bij nieuwe medewerkers (Personio wijst niet automatisch toe op entiteit – zie Tips uit Personio Help) | | | | |
| 7.2 | Verloftypes en regelingen sluiten aan op wetgeving, cao en arbeidsvoorwaarden per entiteit (bijv. wettelijke vs. bovenwettelijke vakantiedagen in NL) | | | | |
| 7.3 | Opbouw, meenemen naar volgend jaar en vervaldatum zijn ingericht en kloppen | | | | |
| 7.4 | Opbouw is pro rata ingericht voor parttimers en in-/uitdiensttreding in de loop van het jaar | | | | |
| 7.5 | De goedkeuringsroute voor verlofaanvragen is ingericht (bijv. manager, met vervanger bij afwezigheid) | | | | |
| 7.6 | Verlofsaldi gaan correct naar payroll (bijv. uitbetaling bij uit dienst) – zie module 13 | | | | |

### Verzuim

| # | Controlepunt | Score (0-3) | Bevinding | Advies | Prio |
|---|--------------|-------------|-----------|--------|------|
| 7.7 | Ziekmeldingen en herstelmeldingen worden in Personio geregistreerd | | | | |
| 7.8 | Er is een workflow die ziekmeldingen signaleert bij de juiste personen (manager, HR, evt. arbodienst) | | | | |
| 7.9 | De workflow signaleert patronen, bijv. frequent verzuim (zoals 3× of vaker ziek in 12 maanden) | | | | |
| 7.10 | Voor langdurig verzuim zijn taken met deadlines ingericht volgens de Wet verbetering poortwachter (bijv. probleemanalyse week 6, plan van aanpak week 8, eerstejaarsevaluatie, ziekmelding UWV week 42) | | | | |
| 7.11 | Er wordt **geen** diagnose of medische informatie vastgelegd (AVG); alleen wat is toegestaan, zoals ziek/hersteld en verwachte duur | | | | |
| 7.12 | Verzuimgegevens zijn alleen zichtbaar voor rollen die ze nodig hebben (zie module 06) | | | | |
| 7.13 | Verzuimcijfers (percentage, meldingsfrequentie, duur) zijn beschikbaar in rapportages (zie module 14) | | | | |

## Datacheck

- [ ] Medewerkers zonder verlofregeling of met een regeling die niet past bij hun entiteit
- [ ] Negatieve of onrealistisch hoge verlofsaldi
- [ ] Verlofaanvragen die lang op goedkeuring wachten
- [ ] Medewerkers met frequent verzuim in de afgelopen 12 maanden (wordt dit gesignaleerd?)
- [ ] Openstaande langdurige ziektegevallen: zijn de poortwachter-stappen op tijd gezet?
- [ ] Vrije-tekstvelden bij ziekte: staat daar medische informatie in die er niet mag staan?

## Veelvoorkomende hiaten

- Verlofregelingen worden per medewerker met de hand toegewezen, waardoor fouten ontstaan bij nieuwe medewerkers
- Eén regeling voor alle entiteiten, terwijl de regels per land of cao verschillen
- Verzuim wordt alleen geregistreerd, maar niemand krijgt een signaal en patronen worden niet gezien
- Poortwachter-deadlines worden in een eigen agenda of Excel bijgehouden
- Medische informatie in opmerkingen of notities

## Praktijktips

- Geef toegang tot **verlofregelingen op basis van de entiteit**.
- Maak een **workflow** die **ziekmeldingen signaleert** in het systeem en waarmee je **patronen** kunt zien.

## Tips uit Personio Help

_Bron: Personio Help Center en Personio Community (stand oktober 2026). (C) = community-bericht, geen officiële documentatie. Controleer menupaden in de eigen omgeving van de klant._

- **Let op:** er is **geen automatische toewijzing van verlofregelingen op basis van office of entiteit**. Opties: **Quick assign** (alleen bij één regeling per verloftype), toewijzen vanaf **startdatum** (met terugwerkende kracht, kan eerdere regelingen overschrijven) of een **bulkimport**. Leg dus een vaste werkwijze vast bij nieuwe medewerkers. ([bron](https://support.personio.de/hc/en-us/articles/30695472069917), [C](https://community.personio.com/personio-tips-best-practices-137/automatically-assigning-time-off-policies-for-newjoiner-5003))
- Per verloftype stel je in: halve dagen, **vervanger** (uit / optioneel / verplicht), **verklaring/certificaat** en of **goedkeuring** nodig is. ([bron](https://developer.personio.de/changelog/absence-api-absence-type-configuration))
- (C) Goedkeuringen kunnen **meerstaps** zijn (bijv. eerst leidinggevende, dan HR); de stappen lopen na elkaar. ([bron](https://community.personio.com/employee-roles-approvals-88/absences-approval-workflow-2157))
- (C) **Meenemen naar volgend jaar** stel je in bij de opbouwregeling (vervaltermijn in maanden). Een regeling die al is toegewezen kun je niet direct aanpassen. Meegenomen dagen worden eerst opgemaakt. ([bron](https://community.personio.com/time-off-attendance-87/ablaufdatum-urlaubsanspruch-aendern-3504))
- (C) **Workflows** kunnen starten bij het aanmaken van een afwezigheid, met voorwaarden (bijv. langer dan N dagen), en sturen meldingen of taken. Let op: losse dagen triggeren elk apart, aaneengesloten dagen één keer. Een signaal bij bijv. de 3e ziekmelding in 12 maanden is genoemd als mogelijkheid – test dit bij de klant. ([bron](https://community.personio.com/time-off-attendance-87/workflow-creation-sickness-absence-instances-5021))

## Opleverpunten voor de klant

- Overzicht verlofregelingen per entiteit (type, opbouw, meenemen, vervaldatum, goedkeuring)
- Opzet verzuimworkflow: signalering, frequent verzuim, poortwachter-taken met deadlines
- Aandachtspunten AVG voor het registreren van verzuim
