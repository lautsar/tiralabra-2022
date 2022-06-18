# Testausdokumentti

Ohjelmaa on testattu unittest-sovelluskehyksen avulla.

## Yksikkötestauksen kattavuusraportti
Tilanne 12.6.

![Testikattavuus](/dokumentaatio/kuvat/testikattavuus.png)

Testikattavuusraportin voi muodostaa komennoilla, jolloin raportti muodostuu *htmlcov*-hakemistoon
```
coverage run --branch -m pytest src
coverage html
```

## 

Testiluokka TestResult testaa lisäksi muiden luokkien yhteistoimintaa.

## Testien toistettavuus

Ohjelman yksikkötestit voidaan suorittaa komennolla
```
poetry run pytest src
```


