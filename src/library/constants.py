import math

class Constants():
    """Luokka hallitsee käyttäjän tallettamia muuttujia.
    """
    def __init__(self):
        """Luokan konstruktori, joka kokoaa käytettävissä olevat vakiot listaan.
        """
        self.constants = []
        self.add_constants()

    def get_value(self, key):
        """Palauttaa parametrina saadun vakion numeerisen arvon.
        """
        for constant in self.constants:
            if constant[0] == key:
                return constant[1]
        
        return False

    def list_usable_constants(self):
        """Palauttaa listan kaikista käytettävissä olevista vakioista.
        """
        used = []
        for constant in self.constants:
            used.append(constant[0])
        
        return used
    
    def add_constants(self):
        """Lisää käytettävissä olevat vakiot listaan vakio-arvo-tuplena.
        """
        self.constants.append(('pi', math.pi))
        self.constants.append(('e', math.e))