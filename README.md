# Tiralabra 2022 - tieteellinen laskin

Tämä projekti on Helsingin yliopiston kurssin *TKT20010 Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit*  harjoitustyö. Projektissa toteutetaan tieteellinen laskin.

## Viikkoraportit
* [Viikko 1](/dokumentaatio/viikkoraportti_1.md)
* [Viikko 2](/dokumentaatio/viikkoraportti_2.md)
* [Viikko 3](/dokumentaatio/viikkoraportti_3.md)
* Viikko 4, ei palautettu
* [Viikko 5](/dokumentaatio/viikkoraportti_5.md)
* [Viikko 6](/dokumentaatio/viikkoraportti_6.md)

## Dokumentaatio
* [Määrittelydokumentti](/dokumentaatio/maarittelydokumentti.md)
* [Testausdokumentti](/dokumentaatio/testausdokumentti.md)
* [Käyttöohje](/dokumentaatio/kayttoohje.md)
* [Toteutusdokumentti](/dokumentaatio/toteutusdokumentti.md)

## Komentorivikomennot

Riippuvuudet voi asentaa komennolla
```
poetry install
```

Sovelluksen voi käynnistää komennolla
```
poetry run python3 src/index.py
```

Testit voi suorittaa komennolla
```
poetry run pytest src
```

Testikattavuusraportin voi muodostaa komennoilla
```
coverage run --branch -m pytest src
coverage html
```
Raportti muodostuu *htmlcov*-hakemistoon

Tiedoston [.pylintrc](.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:
```
poetry run pylint src
```
