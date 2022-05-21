import re
from structures.stack import Stack

class ShuntingYard():
    """Luokka, joka toteuttaa shunting yard -algoritmin.
    """
    def __init__(self):
        """Luokan konstruktori
        """
        self.output = []
        self.operator_stack = Stack()

    def shunting_yard(self, expression):
        """Muutaa infix-notaatiossa olevan lausekkeen postfix-muotoon.

        Args:
            lauseke: Muutettava lauseke

        Returns:
            Muutettu lauseke
        """
        self.output = []
        self.operator_stack = Stack()
        splitted_input = expression.split()

        self.read_tokens(splitted_input)
        self.read_operators()

        print(self.output)

        return self.output

    def read_tokens(self, expression):
        """Lukee algoritmin saaman lausekkeen ja jakaa sen alkiot output-jonoon ja
        operaattoripinoon.

        Args:
            input: Muutettava lauseke
        """
        for token in expression:
            if re.findall("^[0-9]+$", token):
                #print("numero")
                self.output.append(token)
            elif token in ('+', '-', '/', '*', '^'):
                #print('operaattori')
                while not self.operator_stack.is_empty():
                    if self.operator_stack.peek() != '(':
                        self.output.append(self.operator_stack.pop())
                    else:
                        break

                self.operator_stack.push(token)

            elif token == '(':
                #print('vasen sulku')
                self.operator_stack.push(token)
            elif token == ')':
                #print('oikea sulku')
                if self.operator_stack.is_empty():
                    print('väärä määrä sulkuja')
                    return False

                while not self.operator_stack.is_empty() and self.operator_stack.peek() != '(':
                    self.output.append(self.operator_stack.pop())

                if self.operator_stack.is_empty() is False and self.operator_stack.peek() == '(':
                    self.operator_stack.pop()

            else:
                print('virhe')
                return False

            print(f"Output: {self.output}, stack {self.operator_stack.get_stack()}")

    def read_operators(self):
        """Lukee operaattorit operaattoripinosta output-jonoon.
        """
        for token in self.operator_stack.get_stack():
            operator = self.operator_stack.pop()
            if operator == '(':
                print('väärä määrä sulkuja')
                return False
            else:
                self.output.append(token)
