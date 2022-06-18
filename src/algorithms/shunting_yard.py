import re
from structures.stack import Stack

class ShuntingYard():
    """Luokka, joka toteuttaa shunting yard -algoritmin.
    """
    def __init__(self, library):
        """Luokan konstruktori
        """
        self.output = []
        self.operator_stack = Stack()
        self.library = library

    def shunting_yard(self, expression):
        """Muutaa infix-notaatiossa olevan lausekkeen postfix-muotoon.
        Kutsuu ensin metodia split_expression, joka pilkkoo käyttäjän syöttämän lausekkeen
        käsiteltäviin osiin. Tämän tuottama lauseke annetaan metodille read_tokens,
        joka käsittelee lausekkeen osat shunting yard-algoritmin mukaisesti. Lopuksi
        metodi read_operators käsittelee jäljelle jäävän operaattorit.

        Args:
            lauseke: Muutettava lauseke

        Returns:
            Muutettu lauseke, jos syötteenä ollut lauseke on kelvollinen.
            False, jos siinä on jokin ongelma.
        """
        self.output = []
        self.operator_stack = Stack()
        splitted_input = self.split_expression(expression)

        if self.read_tokens(splitted_input) is False:
            return False

        if self.read_operators() is False:
            return False

        print(f"Muutettu lauseke: {self.output}")

        return self.output

    def split_expression(self, expression):
        """Pilkkoo käyttäjän syöttämän lausekkeen osiin.

        Args:
            expression: Käyttäjän syöttämä lauseke

        Returns:
            Lausekkeen osat taulukkona.
        """
        splitted_input = []
        last_char = ''
        last_type = 0
        last_token = ''

        for char in expression:
            if char in ['(', ')', ','] or char in self.library.get_operators() or\
                re.findall(r'\s', char):
                if char == '-' and last_char == '(':
                    last_token = last_token + char
                    last_type = 1

                if last_type != 0:
                    splitted_input.append(last_token)
                    last_token = ''
                    last_type = 0

                if not re.findall(r"\s", char):
                    splitted_input.append(char)
            elif re.findall("[0-9]|[a-z]|.", char):
                last_token = last_token + char
                last_type = 1
            else:
                return False

            if not re.findall(r"\s", char):
                last_char = char

        if last_token != '':
            splitted_input.append(last_token)

        return splitted_input

    def read_tokens(self, expression):
        """Lukee algoritmin saaman lausekkeen ja jakaa sen alkiot output-jonoon ja
        operaattoripinoon.

        Args:
            input: Muutettava lauseke
        """
        for token in expression:
            if re.findall("^[-+]?[0-9]+([.][0-9]+)?$", token):
                self.output.append(token)
            elif token in self.library.get_variables():
                self.output.append(token)
            elif token in self.library.get_constants():
                self.output.append(token)
            elif token in self.library.get_operators():
                self.handle_operator_token(token)
            elif token in self.library.get_functions():
                self.operator_stack.push(token)
            elif token == '(':
                self.operator_stack.push(token)
            elif token == ')':
                if self.operator_stack.is_empty():
                    print('Virheellinen lauseke')
                    return False

                while not self.operator_stack.is_empty() and self.operator_stack.peek() != '(':
                    self.output.append(self.operator_stack.pop())

                if self.operator_stack.is_empty() is False and self.operator_stack.peek() == '(':
                    self.operator_stack.pop()

                if self.operator_stack.peek() in self.library.get_functions():
                    self.output.append(self.operator_stack.pop())

            elif token == ',':
                continue

            else:
                print('Virheellinen lauseke')
                return False

    #        print(f"Output: {self.output}, stack {self.operator_stack.get_stack()}")

    def handle_operator_token(self, token):
        """Käsittelee lausekkeesta tulevat operaattorit siten, että ne käsitellään oikeassa
        järjestyksessä.

        Args:
            token: Käsiteltävä operaattori
        """
        while not self.operator_stack.is_empty():
            if self.operator_stack.peek() not in self.library.get_functions() and\
                self.operator_stack.peek() != '(' and (
                (self.get_precedence(self.operator_stack.peek())[0] > self.get_precedence(token)[0])
                or
                ((self.get_precedence(self.operator_stack.peek())[0] == self.get_precedence(token)[0]) and
                (self.get_precedence(self.operator_stack.peek())[1] == "left"))
            ):

                self.output.append(self.operator_stack.pop())
            else:
                break

        self.operator_stack.push(token)

    def read_operators(self):
        """Lukee operaattorit operaattoripinosta output-jonoon.
        """
        while not self.operator_stack.is_empty():
            operator = self.operator_stack.pop()
            if operator == '(':
                print('Väärä määrä sulkuja')
                return False

            self.output.append(operator)

    def get_precedence(self, operator):
        """Tarkistaa operaattorin laskujärjestyksen.

        Args:
            operator: Operaattori, jonka laskujärjestys tarkistetaan.

        Returns:
            Tuplen, jossa on operaattorin laskujärjestystä kuvaava arvo ja laskujärjestyksen
            suunta. False, jos operaattoria ei ole olemassa.
        """
        if operator in ('+', '-'):
            return (2, "left")
        if operator in ('*', '/'):
            return (3, "left")
        if operator == '^':
            return (4, "right")

        return False
