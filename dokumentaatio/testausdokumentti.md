# Testausdokumentti

Ohjelmaa on testattu unittest-sovelluskehyksen avulla. Ohjelman jokainen luokka on testattu vastaavalla testiluokalla. Lisäksi yksi testiluokka huolehtii kaikkien luokkien yhteistoiminnan testaamisesta.

Ohjelman kokonaistoimintaa on testattu myös manuaalisesti. Ohjelman index.py-tiedostossa sijaitseva tekstikäyttöliittymä on rajattu testikattavuusraportin ulkopuolelle.

## Yksikkötestauksen kattavuusraportti
Tilanne 12.6.

![Testikattavuus](/dokumentaatio/kuvat/testikattavuus.png)

Testikattavuusraportin voi muodostaa komennoilla, jolloin raportti muodostuu *htmlcov*-hakemistoon
```
coverage run --branch -m pytest src
coverage html
```

## Testien tiedot

Kutakin ohjelman luokkaa on testattu vastaavalla testiluokalla. Algoritmiluokkia Evaluator ja ShuntingYard on testattu vastaavilla testiluokilla TestEvaluator ja TestShuntingYard. Lisäksi Evaluator-luokan matemaattiset funktiot on testattu erikseen luokalla TestEvaluatorFunctions. Library-pakkauksen luokkia on testattu vastaavilla testiluokilla, samoin Stack-luokkaa.

Testiluokka TestResult testaa lisäksi muiden luokkien yhteistoimintaa.

Yksikkötesteillä on pyritty testaamaan kattavasti erilaisia syötteitä ja mahdollisia virhetilanteita.

## Testien toistettavuus

Ohjelman yksikkötestit voidaan suorittaa komennolla
```
poetry run pytest src
```


