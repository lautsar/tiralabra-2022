class Stack():
    """Luokka, joka toteuttaa pino-rakenteen.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden pinon.
        """
        self.stack = []
        self.top = -1

    def push(self, token):
        """Lisää alkion pinoon.

        Args:
            token: Pinoon lisättävä alkio.
        """
        self.stack.append(token)
        self.top += 1

    def pop(self):
        """Poistaa pinon päällimmäisen alkion ja palauttaa sen.

        Returns:
            False, jos pino on tyhjä. Muussa tapauksessa pinon päällä olevan alkion.
        """
        if self.is_empty():
            return False

        token = self.stack.pop()

        self.top -= 1

        return token

    def peek(self):
        """Kertoo pinon päällimmäisen alkion arvon.

        Returns:
            False, jos pino on tyhjä. Muussa tapauksessa pinon päällä olevan tokenin.
        """
        if self.is_empty():
            return False

        return self.stack[self.top]

    def is_empty(self):
        """Kertoo, onko pino tyhjä.

        Returns:
            True, jos pino tyhjä, false, jos ei ole.
        """
        return self.top < 0

    def get_stack(self):
        """Palauttaa kysyjälle pinon.

        Returns:
            Taulukon, johon pino on muodostettu.
        """
        return self.stack
