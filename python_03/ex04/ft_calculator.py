class calculator:
    """vector/matrix calculation class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """dot product"""
        lst_res = [i * j for i, j in zip(V1, V2)]
        res = 0
        for x in lst_res:
            res += x
        print('Dot product is:', res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """vector addition"""
        print('Add Vector is :', [float(i + j) for i, j in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """vector subtraction"""
        print('Sous Vector is:', [float(i - j) for i, j in zip(V1, V2)])
