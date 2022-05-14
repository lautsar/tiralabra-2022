# Määrittelydokumentti

## Perustiedot 
Tekijä: Sari Lautanala

Koulutusohjelma: Tietojenkäsittelytieteen kandidaatti

Projektissa käytettävä ohjelmointikieli: python (vertaisarviointia ajatellen osaan myös javan perusteet)

Dokumentaation kieli: suomi

## Projektin aihe

Projektissa toteutetaan tieteellinen laskin, joka laskee käyttäjän antaman matemaattisen lausekkeen arvon. Annettu lauseke voi sisältää:
* lukuarvoja
* muuttujia
* peruslaskutoimituksia
* erilaisia funktioita
Lausekkeen tulos voidaan tallentaa muuttujaan, jota voidaan hyödyntää seuraavissa lausekkeissa.

Käyttäjä antaa matemaattiseen lausekkeen nk. infix-notaatiossa, joka muutetaan shunting yard -algoritmin avulla postfix-notaatioon, arvo evaluoidaan ja palautetaan käyttäjälle. 

## Käytettävät algoritmit ja tietorakenteet (tarkennetaan myöhemmin)

Ohjelmassa toteutetaan shunting yard -algoritmi, joka muuttaa infix-notaatiomuotoisen lausekkeen postfix-notaatiomuotoiseksi lausekkeeksi. Shunting yard -algoritmin aikavaativuus on O(n), sillä algoritmi käy annetun syötteen läpi alusta loppuun tasan kerran.

Lisäksi tarvitaan algoritmi, joka laskee shunting yard -algoritmin muodostaman lausekkeen arvon. 

Sekä shunting yard -algoritmissa käytetään jono- ja pinotietorakenteita. Myös postfix-muotoisen lausekkeen evaluoinnissa käytetään pino-tietorakennetta.

## Lähteet (tarkennetaan myöhemmin)
[Shunting yard algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)

[Infix notation (Wikipedia)](https://en.wikipedia.org/wiki/Infix_notation)