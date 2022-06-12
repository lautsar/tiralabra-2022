# Viikkoraportti 5

(Kahden katastrofiviikon jälkeen työ on vihdoin edennyt varsin mukavasti. Dokumentaation päivitys jäi vielä vaiheeseen lauantain deadlineen mennessä. Päivitän dokumentoinnin sunnuntain aikana.)

## Tällä viikolla tehtyä
* Shunting yard -algoritmin perustoiminnan viimeistely, kaikki peruslaskutoimitukset onnistuvat oikein
* Matemaattisten funktioiden ja vakioiden käyttöönoton aloitus
* Mahdollisuus tallentaa lausekkeen tulos muuttujaan ja käyttää muuttujan arvoa lausekkeessa
* Uusien luokkien testaus
* Hyvin alkeellinen käyttöliittymä
* Dokumentaation päivitys
* Tällä viikolla projektiin käytetty aika: 25 h

## Ohjelman edistyminen

Tällä viikolla ohjelma edistyi varsin mukavasti, mikä tosin oli välttämätöntä, koska parin edellisen viikon aikana ohjelma ei edennyt juuri ollenkaan.

Shunting yard -algoritmin perustoiminnan ja sen tuottaman lausekkeen evaluonnin pitäisi nyt olla kunnossa. Kaikki perusoperaattorit toimivat oikein, ja toteutin tällä viikolla myös omat luokat matemaattisille vakioille, funktioille ja käyttäjän tallentamille muuttujille. Myös näitä voi käyttää lausekkeessa ja algoritmi käsittelee ne (nähdäkseni) oikein.

## Tämän viikon opit

Vielä tarkempi tutustuminen shunting yard -algoritmiin auttoi korjaamaan viimeiset ongelmat laskujärjestyksessä. Sain myös konkreettisen muistutuksen koodin rakenteen suunnittelusta ja yksikkötestauksen tärkeydestä, kun löysin koodista bugin, jonka kuvittelin testanneeni yksikkötestillä.

Lisäksi luin hieman materiaalia ensimmäistä vertaisarviointia varten itselleni vieraista trie-rakenteesta ja Markovin ketjuista.

## Tämän viikon haasteet

Ei suuria haasteita.

## Mitä seuraavaksi

Seuraavaksi yritän järkeistää shunting yard- ja evaluator-luokkien rakennetta. Kumpikin luokka koostuu hieman epämääräisistä if-else-rakenteista, joiden testaaminenkin on vaikeaa.