# LogBook
Zapisovalnik in sledilnik obveznosti katerih je potrebno opraviti tekom študija.

# Okolje
``` cmd
python -m venv .venv
source .venv/bin/activate
```

Inštalacija dodatnih knjižnic:
```cmd
python3 pip install -r requirements.txt
```

# Zagon
Ob prvem zagonu je potrebno inicializirati bazo in uvoziti podatke. Zaženite main.py. 
Ko uporabljate aplikacijo in ob ponovnem zagonu želite obdržati novo stanje baze zaženite main.py tako,
da parametre nastavite na initialize_db(wipeout=False, data_import=False).

## CLI
Run cli.py file

## Spletni vmesnik
1. run web-interface.py file
2. zaženi LogBookClient aplikacijo

## Funkcionalnosti
### Tekstovni vmesnik:
- [x] Ustvari nov predmet
- [x] Prikaži seznam vseh predmetov
- [x] Prikaži seznam vseh obveznosti za predmet
- [x] Tabelarični prikaz agregiranih obveznostih po tipu za predmet

### Spletni vmesnik:
#### Dashboard: 
- [x] Odštevalnik dnevov do obveznosti
- [x] Feed - seznam zadnjih 5 dodanih Logov
- [x] Study trend - graf, ki prikazuje skupno število ur dela za faks po dnevih
- [x] Subject study ratio - tortni diagram, ki prikazuje razmerja skupnih ur učenja po predmetih
- [x] Subject - stolpični diagram, ki prikazuje vsoto ur učenja po predmetih
- [x] Assessments - Tabela obveznosti za predmet agregiranih po tipu obveznosti
- [x] Gumb za kreiranje novega loga
- [x] Stat card 1 (Currently working on) - Izpiše predmet in naslov obveznosti na kateri sem nazadnje delala
  - Informacijo pridobi iz zadnjega loga, ki ima tip Track in najkasnejši trackedFrom
- [x] Stat card 2 (Completed Assessments Counter) - Izpiše število zaključenih obveznosti / število vseh obveznosti (razmerje v procentih)
- [x] Stat card 3 (Study hours Counter) - Izpiše vsoto vseh ur učenja
- [x] Stat card 4 (Coming up) - Izpiše predmet in naslov obveznosti, katera je najbližje

#### Assessments: 
- [x] Tabela obveznosti
- [x] Gumb za kreiranje nove obveznosti

#### General:
- [x] gumb za nastavitev teme (temna ali svetla)
- [x] Logo gumb, ki vodi do Dashboarda

## Entity Relationship diagram

## Tech stack
- Bottle


