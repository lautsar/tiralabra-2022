# Viikkoraportti 2

## Tällä viikolla tehtyä
* Tarkempi tutustuminen shunting yard -algoritmiin
* Hyvin karkea runko shunting yard -algoritmille, jonka avulla tutustuin algoritmin perustoimintaan
* Runko lausekkeen arvon laskevalle algoritmille
* Pinon toteuttavan luokan rakennus
* Ensimmäiset testit
* Tällä viikolla projektiin käytetty aika: 10 h (Tarkempi [tuntikirjanpito](tuntikirjanpito.md))

## Ohjelman edistyminen
Tällä viikolla kirjoitin ensimmäiset rivit koodia ja niille testejä. Sain luotua shunting yard -algoritmille sekä sen tuottaman lausekkeen evaluoinnin tekeville algoritmeille toimivan rungon. Lisäksi toteutin ensimmäisen version pino-tietorakenteen luovasta luokasta.

Pääsääntöisesti keskityin algoritmin perustoimintoihin, joten monessa muussa kohdassa on vielä oiottu. Esimerkiksi luettava merkkijono toimii tällä hetkellä vain niin, että jokaisen eri osan välillä on välilyönti, jolloin string-luokan valmis split-metodi käsittelee merkkijonon suoraan. Myös esim. shunting yard -algoritmin tämän hetkinen versio käsittelee vielä kaikki operaattorit vasemmalta oikealle riippumatta siitä, mikä niiden oikea laskujärjestys on.

## Tämän viikon opit
Shunting yard -algoritmin perustoiminta

## Tämän viikon haasteet
Ei suurempia ongelmia.

## Mitä seuraavaksi
Jatkan shunting yard -algoritmin parissa, jotta kaikki peruslaskutoimitukset saadaan laskettua oikeassa järjestyksessä. Alan pohtia arvojen tallennusta muuttujaan ja niiden hyödyntämistä algoritmissa, samoin erilaisten funktioiden laskemista.