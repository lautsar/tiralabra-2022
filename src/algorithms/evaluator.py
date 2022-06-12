import re
import math
from structures.stack import Stack

class Evaluator():
    """Luokka vastaa Shunting yard -algoritmin tuottaman lausekkeen arvon laskemisesta.
    """
    def __init__(self, library):
        """Luokan konstruktori, joka luo luokan käyttämän pinon. Saa parametrina
        kirjasto-olion, joka huolehtii operaattoreista.
        """
        self.stack = Stack()
        self.library = library
        self.take_two = ['+', '-', '/', '*', '^', 'min', 'max']
        self.take_one = ['sqrt', 'sin', 'cos', 'tan']

    def evaluate(self, output):
        self.stack = Stack()

        for token in output:
            if re.findall("^[-+]?[0-9]+([.][0-9]+)?$", token):
                self.stack.push(float(token))
            elif token in self.library.get_constants():
                self.stack.push(self.library.get_constant_value(token))
            elif token in self.library.get_variables():
                self.stack.push(self.library.get_variable_value(token))
            elif token in self.take_two:
                a = self.stack.pop()
                b = self.stack.pop()

                if token == '+':
                    self.stack.push(float(a) + float(b))
                elif token == '-':
                    self.stack.push(float(b) - float(a))
                elif token == '/':
                    self.stack.push(float(b) / float(a))
                elif token == '*':
                    self.stack.push(float(a) * float(b))
                elif token == '^':
                    self.stack.push(float(b)**float(a))
                elif token == 'min':
                    self.stack.push(min(float(a), float(b)))
                elif token == 'max':
                    self.stack.push(max(float(a), float(b)))
                else:
                    return False
            elif token in self.take_one:
                a = self.stack.pop()

                if token == 'sin':
                    self.stack.push(math.sin(float(a)))
                elif token == 'cos':
                    self.stack.push(math.cos(float(a)))
                elif token == 'tan':
                    self.stack.push(math.tan(float(a)))
                elif token == 'sqrt':
                    if a < 0:
                        return False
                    self.stack.push(math.sqrt(float(a)))
            else:
                return False

#            print(self.stack.get_stack())

        return self.stack.get_stack()[0]
