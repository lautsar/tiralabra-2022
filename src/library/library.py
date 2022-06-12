from library.constants import Constants
from library.variables import Variables
from library.functions import Functions

class Library():
    """Luokka kokoaa yhteen paikkaan muuttujien, vakioiden ja funktioiden
    hallinnan. Se luo näitä vastaavat oliot ja kutsuu niiden avulla
    varsinaisten olioiden tuottamia palveluita.
    """
    def __init__(self):
        self.variables = Variables()
        self.constants = Constants()
        self.functions = Functions()
        self.basic_operators = ['+', '-', '/', '*', '^']

    def get_variables(self):
        return self.variables.list_used_variables()

    def get_variable_value(self, variable):
        return self.variables.get_value(variable)

    def get_constants(self):
        return self.constants.list_usable_constants()

    def get_constant_value(self, constant):
        return self.constants.get_value(constant)

    def get_functions(self):
        return self.functions.list_usable_functions()

    def get_operators(self):
        return self.basic_operators

    def list_all_usable_things(self):
        print(f"Käytössä olevat muuttujat: {self.get_variables()}")
        print(f"Käytössä olevat vakiot: {self.get_constants()}")
        print(f"Käytössä olevat funktiot: {self.get_functions()}")
        print(f"Käytössä olevat perusoperaattorit: {self.get_operators()}")

    def add_variable(self, key, value):
        return self.variables.add_variable(key, value)
