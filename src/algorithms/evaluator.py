import re
from structures.stack import Stack
import math

class Evaluator():
    def __init__(self):
        self.stack = Stack()
        self.constants = ['pi']
        self.take_two = ['+', '-', '/', '*', '^', 'min', 'max']

    def evaluate(self, output):
        self.stack = Stack()

        for token in output:
            if re.findall("^[0-9]+$", token):
                self.stack.push(int(token))
            elif token in self.constants:
                if token == 'pi':
                    self.stack.push(math.pi)
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
            else:
                a = self.stack.pop()

                if token == 'sin':
                    self.stack.push(math.sin(float(a)))
                elif token == 'cos':
                    self.stack.push(math.cos(float(a)))
                elif token == 'tan':
                    self.stack.push(math.tan(float(a)))

            print(self.stack.get_stack())

        return self.stack.get_stack()[0]
