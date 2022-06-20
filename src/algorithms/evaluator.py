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
        self.take_one = ['sqrt', 'sin', 'cos', 'tan', 'abs']

    def evaluate(self, output):
        if len(output) == 0:
            return False

        self.stack = Stack()

        for token in output:
            if re.findall("^[-+]?[0-9]+([.][0-9]+)?$", token):
                self.stack.push(float(token))
            elif token in self.library.get_constants():
                self.stack.push(self.library.get_constant_value(token))
            elif token in self.library.get_variables():
                self.stack.push(self.library.get_variable_value(token))
            elif token in self.take_two:
                if self.take_two_values(token) is False:
                    return False
            elif token in self.take_one:
                if self.take_one_value(token) is False:
                    return False
            else:
                return False

        return self.stack.get_stack()[0]

    def take_two_values(self, token):
        """ Laskee arvon sellaisille operaatiolle, jotka ottavat kaksi arvoa, ja
        lisää sen pinoon.

        Args:
            token: Käsiteltävä operaattori

        Returns:
            False, jos operaatio on tuntematon tai sitä ei voida laskea.
            Muuten True,
        """
        a = self.stack.pop()
        b = self.stack.pop()

        if a is False or b is False:
            return False

        if token == '+':
            self.stack.push(float(a) + float(b))
        elif token == '-':
            self.stack.push(float(b) - float(a))
        elif token == '/':
            if a == 0:
                return False
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

        return True

    def take_one_value(self, token):
        """ Laskee arvon sellaisille operaatiolle, jotka ottavat yhden arvon, ja
        lisää sen pinoon.

        Args:
            token: Käsiteltävä operaattori

        Returns:
            False, jos operaatio on tuntematon tai sitä ei voida laskea.
            Muuten True,
        """
        a = self.stack.pop()

        if a is False:
            return False

        if token == 'sin':
            self.stack.push(math.sin(float(a)))
        elif token == 'cos':
            self.stack.push(math.cos(float(a)))
        elif token == 'tan':
            self.stack.push(math.tan(float(a)))
        elif token == 'abs':
            if a < 0:
                self.stack.push(float(-a))
            else:
                self.stack.push(float(a))
        elif token == 'log':
            if a < 0:
                return False
            self.stack.push(math.log10(float(a)))
        elif token == 'ln':
            if a < 0:
                return False
            self.stack.push(math.log(float(a)))
        elif token == 'sqrt':
            if a < 0:
                return False
            self.stack.push(math.sqrt(float(a)))
        else:
            return False

        return True
