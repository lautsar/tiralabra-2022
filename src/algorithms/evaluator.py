import re
from structures.stack import Stack

class Evaluator():
    def __init__(self):
        self.stack = Stack()

    def evaluate(self, output):
        self.stack = Stack()

        for token in output:
            if re.findall("^[0-9]+$", token):
                self.stack.push(int(token))
            else:
                a = self.stack.pop()
                b = self.stack.pop()

                if token == '+':
                    self.stack.push(int(a) + int(b))
                elif token == '-':
                    self.stack.push(int(b) - int(a))
                elif token == '/':
                    self.stack.push(int(b) / int(a))
                elif token == '*':
                    self.stack.push(int(a) * int(b))
                elif token == '^':
                    self.stack.push(int(b)**int(a))
                else:
                    return False

            print(self.stack.get_stack())

        return self.stack.get_stack()[0]
