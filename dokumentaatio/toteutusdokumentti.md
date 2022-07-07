# Toteutusdokumentti

## Ohjelman yleisrakenne

Algorithms-pakkauksessa olevat luokat huolehtivat algoritmien toiminnasta: ShuntingYard toteuttaa shunting yard -algoritmin ja Evaluator huolehtii algoritmin tuottaman lausekkeen arvon laskennasta. Structures-pakkauksessa oleva luokka Stack toteuttaa pinorakenteen, jota algoritmit käyttävät. Library-pakkauksessa olevat luokat Constants, Functions ja Variables huolehtivat vakioiden, funktioiden ja muuttujien hallinnasta. Library-luokkaa tarjoaa näiden luokkien tarjoamat palvelut algoritmeille.

Käyttöliittymä on toteutettu suoraan index.py-tiedostoon sen yksinkertaisuuden takia.

## Saavutetut aika- ja tilavaativuudet

Työssä toteutettiin kaksi algoritmia: Shunting yard -algoritmi ja sen tuottaman lausekkeen evaluoiva algoritmi. Kummankin algoritmin aikavaativuus on O(n), sillä kumpikin algoritmi käy tasan kerran läpi parametrina saamansa syötteen.

## Puutteet ja parannusehdotukset

Ohjelma kaatuu ylivuototilanteessa OverflowErroriin.
