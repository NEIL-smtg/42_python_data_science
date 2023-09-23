class calculator:
    """calculator class"""
    def __init__(self, vector) -> None:
        """calc init"""
        self.vector = vector

    def __add__(self, object) -> None:
        """add"""
        res = [x + object for x in self.vector]
        self.vector = res
        print(self.vector)

    def __mul__(self, object) -> None:
        """mul"""
        res = [x * object for x in self.vector]
        self.vector = res
        print(self.vector)

    def __sub__(self, object) -> None:
        """sub"""
        res = [x - object for x in self.vector]
        self.vector = res
        print(self.vector)

    def __truediv__(self, object) -> None:
        """div"""
        try:
            err_msg = 'AssertionError: Division by 0 is not allowed'
            assert float(object) != 0.0, err_msg
        except AssertionError as msg:
            print(msg)
            return
        res = [x / object for x in self.vector]
        self.vector = res
        print(self.vector)
