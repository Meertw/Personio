# 13 – Payroll & integraties

> **Waarom belangrijk?** Alles wat in de modules hiervoor is ingericht (attributen, salaris, verlof, tijd, commissies) komt hier samen in de salarisverwerking. Fouten in de inrichting worden hier zichtbaar als fouten in de loonstrook.

## Controlepunten

| # | Controlepunt | Score (0-3) | Bevinding | Advies | Prio |
|---|--------------|-------------|-----------|--------|------|
| 13.1 | Het is duidelijk welke gegevens van Personio naar het payrollsysteem gaan (bijv. Nmbrs) en hoe (koppeling of export) | | | | |
| 13.2 | De voorlopige payroll (preliminary payroll) wordt elke periode goedgekeurd vóór de export | | | | |
| 13.3 | Wijzigingen halverwege een periode worden correct verwerkt | | | | |
| 13.4 | Payroll-attributen (module 05) zijn volledig en sluiten aan op het payrollsysteem | | | | |
| 13.5 | Bekend is dat payrollproviders eigen validaties hebben (bijv. IBAN); fouten uit de payrollkoppeling worden teruggekoppeld en in Personio opgelost | | | | |
| 13.6 | Verlof, verzuim, overuren en variabele beloning gaan correct mee (modules 07, 08, 12) | | | | |
| 13.7 | Overige koppelingen (SSO, IT, finance, LMS) zijn in kaart gebracht en hebben een eigenaar | | | | |
| 13.8 | API-koppelingen hebben alleen toegang tot de attributen die ze nodig hebben | | | | |
| 13.9 | Workflows (Automations) worden gebruikt om handwerk tussen systemen te verminderen | | | | |

## Datacheck

- [ ] Verschillen tussen Personio en het payrollsysteem (steekproef op salaris, uren, kostenplaats)
- [ ] Niet-goedgekeurde payrollperiodes
- [ ] Lijst van API-credentials en welke attributen ze kunnen lezen

## Veelvoorkomende hiaten

- Exporteren zonder de voorlopige payroll goed te keuren, waardoor wijzigingen verloren gaan
- Gegevens dubbel ingevoerd in Personio en het payrollsysteem
- API-credentials met te veel toegang, of zonder eigenaar

## Antwoorden van Personio

_Bron: schriftelijke antwoorden van Personio na de demosessie (oktober 2026)._

- Een IBAN die Personio goedkeurt, kan door de payrollprovider alsnog worden afgekeurd: de provider kan eigen validatieregels hebben.
- Bonussen op basis van doelrealisatie (module 12) kennen beperkingen bij het overzetten naar Personio Payroll; stem de werkwijze af op de payrollinrichting van de klant.

## Tips uit Personio Help

_Bron: Personio Help Center en Personio Community (stand oktober 2026). (C) = community-bericht, geen officiële documentatie._

- Door de **voorlopige payroll goed te keuren** worden de gegevens bevroren en worden de wijzigingsmarkeringen gereset. **Exporteer je zonder goedkeuren**, dan worden de markeringen aan het begin van de periode gereset en kunnen **wijzigingen verloren gaan**. ([bron](https://support.personio.de/hc/en-us/articles/115003457605))
- Voor Nmbrs is er een helpartikel over het handmatig exporteren van wijzigingen halverwege een periode; ook dan moet de voorlopige payroll worden goedgekeurd. (Exacte link niet bevestigd – te vinden in de payroll-sectie van het Help Center.)
- **API-credentials** maak je via Marketplace > 'Create custom integration'. Je zet per credential vast welke attributen gelezen mogen worden; attributen die niet op die lijst staan (ook eigen attributen) worden **zonder melding weggelaten**. ([bron](https://developer.personio.de/docs))
- **Workflows** (Automations > Workflows) bestaan uit een trigger (tijd, document of medewerkersgebeurtenis), optionele voorwaarden en acties; je kunt starten vanuit een template. ([bron](https://support.personio.de/hc/en-us/articles/16606744442397))
- De Employee API geeft geen attribuuthistorie terug (zie module 05).

## Praktijktips

_Wordt aangevuld vanuit [`tips/tips-log.md`](../tips/tips-log.md)._

## Opleverpunten voor de klant

- Overzicht datastromen Personio ↔ payroll en andere systemen
- Checklist maandelijkse payrollafsluiting
- Overzicht API-credentials en rechten
