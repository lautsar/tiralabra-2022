class Variables():
    """Luokka hallitsee käyttäjän tallettamia muuttujia.
    """
    def __init__(self):
        """Luokan konstruktori, joka luo listan, johon muuttujat tallennetaan.
        """
        self.variables = []

    def add_variable(self, key, value):
        """Lisää parametrina saadun muuttujan ja sen arvon listaan. Jos muuttuja on jo olemassa,
        kutsutaan metodia, joka päivittää muuttujan arvon."""
        if self.get_value(key) is False:
            self.variables.append((key, value))
            return True

        self.update_value(key, value)

    def get_value(self, key):
        """Hakee ja palauttaa parametrina saadun muuttujan arvon.
        Jos muuttujaa ei ole, palautetaan False"""
        for variable in self.variables:
            if variable[0] == key:
                return variable[1]

        return False

    def list_used_variables(self):
        """Palauttaa listan muuttujista, joihin on tallennettu jotain."""
        used = []
        for variable in self.variables:
            used.append(variable[0])

        return used

    def update_value(self, key, value):
        """Päivittää parametrina saadun muuttujan arvon."""
        i = 0
        while i < len(self.variables):
            if self.variables[i][0] == key:
                self.variables[i] = (key, value)
                return True

            i += 1

        return False
