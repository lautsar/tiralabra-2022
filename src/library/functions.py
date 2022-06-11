import math

class Functions():
    """Luokka hallitsee käytettävissä olevia funtioita.
    """
    def __init__(self):
        """Luokan konstruktori. Luo listan käytössä olevista funktioista.
        """
        self.functions = []
        self.add_functions()

    def get_value(self, key):
        """Palauttaa parametrina saadun funktion tarvitsemien parametrien määrän ja False, jos funktiota ei ole.
        """
        for function in self.functions:
            if function[0] == key:
                return function[1]
        
        return False

    def list_usable_functions(self):
        """Palauttaa listan kaikista käytössä olevista funktioista.
        """
        used = []

        for function in self.functions:
            used.append(function[0])
        
        return used
    
    def add_functions(self):
        """Lisää luokan listaan ne funktiota. Listaan lisätään tuplena funktion nimi ja sen laskentaan tarvittavien parametrien määrä.
        """
        self.functions.append(('min', 2))
        self.functions.append(('max', 2))
        self.functions.append(('sqrt', 1))
        self.functions.append(('sin', 1))
        self.functions.append(('cos', 1))
        self.functions.append(('tan', 1))
