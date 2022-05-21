# Tiralabra 2022 - tieteellinen laskin

Tämä projekti on Helsingin yliopiston kurssin *TKT20010 Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit*  harjoitustyö. Projektissa toteutetaan tieteellinen laskin.

## Viikkoraportit
* [Viikko 1](/dokumentaatio/viikkoraportti_1.md)
* [Viikko 2](/dokumentaatio/viikkoraportti_2.md)

## Dokumentaatio
* [Määrittelydokumentti](/dokumentaatio/maarittelydokumentti.md)
* [Testausdokumentti](/dokumentaatio/testausdokumentti.md)

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
