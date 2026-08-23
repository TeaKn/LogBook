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
## CLI
Run cli.py file

## Spletni vmesnik
1. run web-interface.py file
2. zaženi LogBookClient aplikacijo

## Funkcionalnosti
### Tekstovni vmesnik:
- [ ] Ustvari nov predmet
- [ ] Prikaži seznam vseh predmetov
- [ ] Prikaži seznam vseh obveznosti za predmet
- [ ] Tabelarični prikaz agregiranih obveznostih po tipu za predmet

### Spletni vmesnik:
#### Dashboard: 
- [ ] Odštevalnik dnevov do obveznosti
- [ ] Feed - seznam zadnjih 5 dodanih Logov
- [ ] Study trend - graf, ki prikazuje skupno število ur dela za faks po dnevih
- [ ] Subject study ratio - tortni diagram, ki prikazuje razmerja skupnih ur učenja po predmetih
- [ ] Subject - stolpični diagram, ki prikazuje vsoto ur učenja po predmetih
- [ ] Assessments - Tabela obveznosti za predmet agregiranih po tipu obveznosti
- [ ] Gumb za kreiranje novega loga
- [ ] Stat card 1 (Currently working on) - Izpiše predmet in naslov obveznosti na kateri sem nazadnje delala
  - Informacijo pridobi iz zadnjega loga, ki ima tip Track in najkasnejši trackedFrom
- [ ] Stat card 2 (Completed Assessments Counter) - Izpiše število zaključenih obveznosti / število vseh obveznosti (razmerje v procentih)
- [ ] Stat card 3 (Study hours Counter) - Izpiše vsoto vseh ur učenja
- [ ] Stat card 4 (Coming up) - Izpiše predmet in naslov obveznosti, katera je najbližje

#### Assessments: 
- [ ] Tabela obveznosti
- [ ] Gumb za kreiranje nove obveznosti

#### General:
- [ ] gumb za nastavitev teme (temna ali svetla)
- [ ] Logo gumb, ki vodi do Dashboarda

## Entity Relationship diagram
<img width="730" height="511" alt="image" src="https://github.com/user-attachments/assets/7822dc3f-5676-41cb-a311-23b2759dafaa" />


<img width="709" height="697" alt="er" src="https://github.com/user-attachments/assets/7640c9cc-10c1-4f44-8d2c-e94161a2e29b" />

## Tech stack
- Bottle


