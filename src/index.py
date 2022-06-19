import re
from algorithms.shunting_yard import ShuntingYard
from algorithms.evaluator import Evaluator
from library.library import Library

def main():
    library = Library()
    shunting_yard = ShuntingYard(library)
    evaluator = Evaluator(library)

    print("Syötä laskettava lauseke. Negatiiviset luvut on ympäröitävä suluilla, jotta lasku menee varmasti oikein.")
    print("'q' lopettaa, 'ohje' antaa listan tuetuista vakioista ja funktioista")
    print("Lausekkeen syötön jälkeen tuloksen voi tallentaa muuttujaan a-z,\
        muu syöte ei tallenna mitään")

    while True:
        expression = input("Lauseke: ")

        if expression == 'q':
            break

        if expression == 'ohje':
            library.list_all_usable_things()
        else:
            output = shunting_yard.shunting_yard(expression)

            if output is not False:
                result = evaluator.evaluate(output)
                print(f"Tulos: {result}")

                variable = input("Tallenna tulos antamalla muuttuja (a-z): ")

                if re.findall("[a-z]", variable) and len(variable) == 1:
                    library.add_variable(variable, result)


if __name__ == "__main__":
    main()
