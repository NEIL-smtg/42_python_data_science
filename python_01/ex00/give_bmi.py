import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:

    height_arr = np.array(height)
    weight_arr = np.array(weight)

    try:
        lenNotEqual = "AssertionError: length of both lists are different."
        typeErrMsg = "AssertionError: Elements should be int or float."

        assert height_arr.size == weight_arr.size, lenNotEqual
        assert np.issubdtype(weight_arr.dtype, np.number) and \
            np.issubdtype(height_arr.dtype, np.number), typeErrMsg

        bmi_list = []
        for h, w in zip(height_arr, weight_arr):
            bmi_list.append(w / pow(h, 2))

        return bmi_list
    except AssertionError as msg:
        print(msg)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [e > limit for e in bmi]
