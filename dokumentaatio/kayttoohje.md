# Käyttöohje



Projektin riippuvuuden asennetaan komennolla
```
poetry install
```

Sovelluksen voi käynnistää juurihakemistosta komennolla
```
poetry run python3 src/index.py
```

Ohjelman käynnistyksen jälkeen ohjelma kysyy käyttäjältä lauseketta, kunnes käyttäjä syöttää lopetuskomennon 'lopeta'.

Ohjelma tuntee kolme komentoa:
* ohje: Tulostaa käytettävissä olevat muuttujat ja funktiot.
* tallenna: Tallentaa viimeisenä annetun lausekkeen arvon muuttujaan (a-z). Muuttuja kysytään käyttäjältä.
* lopeta: Lopettaa ohjelman suorittamisen.

Kaikki muut syötteet tulkitaan matemaattiseksi lausekkeeksi, jonka arvoa yritetään laskea. Lauseke voi sisältää numeroita, kaarisulkuja ja erikseen määritettyjä funktioita, muuttujia ja matemaattisia vakioita. Jos lauseke sisältää muita merkkejä, lauseke tulkitaan virheelliseksi ja käyttäjälle annetaan virheilmoitus. Ohjelma tunnistaa matemaattiset funktiot min, max, sqrt, sin, cos, tan, abs, log, ln sekä vakiot pi ja e. Lisäksi voidaan käyttää muuttujia a-z, jos käyttäjä on tallentanut niihin tietoa.

Jos annettu lauseke sisältää vain sallittuja merkkejä, yritetään laskea sen arvo. Jos lauseke on virheellinen, eli sisältää esimerkiksi väärän määrän sulkuja tai kaksi operaattoria peräkkäin, käyttäjälle annetaan virheilmoitus. Jos lauseke on kelvollinen, käyttäjälle palautetaan sen arvo.
