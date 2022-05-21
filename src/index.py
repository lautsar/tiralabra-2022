from algorithms.shunting_yard import ShuntingYard
from algorithms.evaluator import Evaluator

def main():
    shunting_yard = ShuntingYard()
    evaluator = Evaluator()

    while True:
        lauseke = input("Lauseke: ")

        if lauseke == 'q':
            break

        output = shunting_yard.shunting_yard(lauseke)
        result = evaluator.evaluate(output)
        print(f"Tulos: {result}")


if __name__ == "__main__":
    main()
