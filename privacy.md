# Privacyprotocol quickscan

De **klant** is verwerkingsverantwoordelijke; **worldofwork** is verwerker. Uitgangspunt: we beoordelen de **inrichting** van Personio, niet de inhoud van personeelsdossiers, en zien zo min mogelijk persoonsgegevens.

## Afspraken

- Verwerkersovereenkomst vóór de start, met doel, soorten gegevens, bewaartermijn en verwijdering.
- Alleen de consultants die aan de opdracht werken hebben toegang.

## Toegang

- Standaard: **schermdelen** door de HR-beheerder.
- Eigen account alleen als nodig: aparte rol, leesrechten op instellingen, **geen** toegang tot salaris, verzuim, documenten of BSN, en een **einddatum**.
- Geen gedeelde inloggegevens. API-credentials alleen met de attributen die nodig zijn.

## Gegevens

- Bij voorkeur **geaggregeerde cijfers** (aantallen, percentages).
- Exports **zonder namen** en zonder salaris, IBAN, BSN, adres of verzuimreden.
- Gender pay gap: de klant draait het rapport zelf; wij ontvangen alleen de uitkomst.
- Opslag alleen in de **beveiligde klantmap** (bijv. SharePoint met beperkte toegang). Niet lokaal, niet per mail.

## Wat nooit mag

- Klantgegevens, ingevulde scoresheets, exports, klantnamen of screenshots in de **GitHub-repository** (de map `klanten/` wordt door Git genegeerd als vangnet).
- Persoonsgegevens van klanten in AI-tools plakken, tenzij afgedekt in de verwerkersovereenkomst en het eigen beleid.
- Screenshots met persoonsgegevens maken.
- Namen in het rapport.

## Incidenten

Ziet u tijdens de scan een mogelijk datalek of privacyrisico (bijv. iedereen kan salarissen of verzuim zien)? **Direct melden** bij de contactpersoon van de klant en intern bij worldofwork. Niet wachten tot het rapport.

## Afronding

- Account deactiveren, exports verwijderen.
- Klant schriftelijk bevestigen dat toegang is ingetrokken en data is verwijderd.
