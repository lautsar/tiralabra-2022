import re
from algorithms.shunting_yard import ShuntingYard
from algorithms.evaluator import Evaluator
from library.library import Library

def print_instructions():
    print("Käytössä olevat komennot: ")
    print("'lopeta' lopettaa ohjelman")
    print("'ohje' antaa listan tuetuista vakioista ja funktioista")
    print("'tallenna' tallentaa viimeksi lasketun lausekkeen arvon muuttujaan")
    print("Kaikki muu syöte tulkitaan laskettavaksi lausekkeeksi, jonka arvoa yritetään laskea.")
    print("Laskettava lauseke voi sisältää numeroita, sulkuja, perusoperaattoreita, funktioita ja tallennettuja muuttujia")
    print("Negatiiviset luvut on laitettava sulkujen sisään, jotta laskenta toimii oikein")


def main():
    library = Library()
    shunting_yard = ShuntingYard(library)
    evaluator = Evaluator(library)

    latest  = 0

    print_instructions()

    while True:
        expression = input("Lauseke tai komento: ")

        if expression == 'lopeta':
            break

        if expression == 'ohje':
            library.list_all_usable_things()
        elif expression == 'tallenna':
            variable = input("Tallenna viimeisin tulos antamalla muuttuja (a-z): ")
            if re.findall("[a-z]", variable) and len(variable) == 1:
                library.add_variable(variable, latest)
            else:
                print('Virheellinen muuttujan nimi')
        else:
            output = shunting_yard.shunting_yard(expression)

            if output is not False:
                result = evaluator.evaluate(output)
                latest = result
                print(f"Tulos: {result}")
            else:
                print_instructions()

if __name__ == "__main__":
    main()
