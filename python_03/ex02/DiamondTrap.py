from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class"""

    def __init__(self, first_name, is_alive=True):
        """King init"""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """return eyes"""
        return self.eyes

    def set_eyes(self, value):
        """setting eyes to new value"""
        self.eyes = value

    def get_hairs(self):
        """returns hair color"""
        return self.hairs

    def set_hairs(self, value):
        """setting hair color"""
        self.hairs = value

# python using a method resolution order(MRO)
# class hierarchy, king inherits from Baratheon and Lannister
# MRO is determined by the C3 Linearization algorithm
# MRO dictates that when super().__init__(first_name, is_alive)
# get called in this class, it will call the constructor of
# the next class in MRO, which is baratheon
# to bypass MRO, just use Lannister.__init__(self, first_name, is_alive)
