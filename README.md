# LogBook
Zapisovalnik in sledilnik obveznosti katerih je potrebno opraviti tekom študija.

## Motivacija
Obstaja veliko orodij s katerimi si lahko pomagamo vodit projek. Obstajajo tudi orodja, s katerimi imamo lahko dober uvid v podatke. Težavo, ki jo rešujem zase je izboljšati fazo pridobivanja podatkov. Izboljšat to fazo zame pomeni, da porabim manj časa pri zapisaovanju trenutnih podatkov. Podatki, ki jih pridobivam se direktno navezujejo na parametre, za katere se zanimam kako se spreminjajo. 

## Aspiracija (Cilji)
1. LogBook zvišuje motivacijo pri opravljanju potrebnih in ne ravno zaželjenih opravil
2. LogBook olajša evidentiranje vnaprej določenih parametrov
3. LogBook olajša spremljanje vnaprej določenih parametrov

## Tehnični cilji
- [ ] avtomatizirati vnos podatkov / avtomatizacija evidentiranja
- [ ] osnovna gameifikacija opravljanja opravil

## Funkcionalnosti
CRUD predmet:
- [ ] Ustvariš nov predmet (Subject)
- [ ] Spremeniš obstoječi predmet
- [ ] Izbrišeš predmet
- [ ] Pridobiš podatke o predmetu

CRUD evidenca:
- [ ] Ustvariš evidenco (EvidencaPredmetGeneric) za predmet
- [ ] Spremeniš obstoječo evidenco
- [ ] Izbrišeš evidenco
- [ ] Pridobiš podatke o evidenci

CRUD obveznost:
- [ ] Ustvariš obveznost za predemt
- [ ] Spremeniš obstoječo obveznost
- [ ] Izbrišeš obveznost
- [ ] Pridobiš podatke o obveznosti

Tekstovni vmesnik in spletni vmesnik:
- [ ] Pridobi seznam vseh predmetov
- [ ] Pridobi seznam vseh obveznosti za predemet
- [ ] Pridobi seznam vseh obveznosti 

Spletni vmesnik:
- [ ] Odštevalnik dnevov do obveznosti
- [ ] Graf, ki prikazuje število poskuskov za neko opravilo
- [ ] Graf, ki prikazuje komulativno število poskuskov za neko opravilo
- [ ] Seznam trenutnih obveznosti na katerih moram delat ta teden

Mobilni vmesnik:
- cli na telefonu?
- [ ] Shranit data na domači server

## Entity Relationship diagram
<img width="730" height="511" alt="image" src="https://github.com/user-attachments/assets/7822dc3f-5676-41cb-a311-23b2759dafaa" />


<img width="709" height="697" alt="er" src="https://github.com/user-attachments/assets/7640c9cc-10c1-4f44-8d2c-e94161a2e29b" />


## Tech stack
- Bottle

## How to run
1. CLI
   2. Run cli.py file
3. Web interface
   4. RUn web-interface.py file


