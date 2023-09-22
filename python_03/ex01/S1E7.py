from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Baratheon init"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self) -> str:
        """Baratheon __str__"""
        return f"Vector: ('{self.family_name}', '{self.eyes}, {self.hairs})"

    def __repr__(self) -> str:
        """Baratheon __repr__"""
        return self.__str__()

    def die(self):
        """Baratehon die()"""
        super().die()


class Lannister(Character):
    "Lannister class : always pay his debts"

    def __init__(self, first_name, is_alive=True):
        """Lannister init()"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self) -> str:
        """Lannister die()"""
        return f"Vector: ('{self.family_name}', '{self.eyes}, {self.hairs})"

    def __repr__(self) -> str:
        """Lannister die()"""
        return self.__str__()

    def die(self):
        """Lannister die"""
        super().die()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create Lannister"""
        return cls(first_name, is_alive)
