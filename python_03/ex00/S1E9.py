from abc import ABC, abstractmethod


class Character(ABC):
    """Character abstract class"""
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        self.is_alive = False


class Stark(Character):
    """Stark class : Ned stark was too kind"""

    def __init__(self, first_name: str, is_alive=True):
        """Stark constructor : Winter is comming"""
        super().__init__(first_name, is_alive)
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Stark dies : killed by king Joffery"""
        super().die()
