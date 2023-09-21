import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Throw error when not receiving list
    using slicing method in python to sliceeeee
    """
    try:
        errMsg = "AssertionErrror: Only list is acceptable."
        assert isinstance(family, list), errMsg
        arr = np.array(family)
        print("My shape is ", arr.shape)
        print("My new shape is ", arr[start:end].shape)
        return arr[start:end].tolist()
    except AssertionError as msg:
        print(msg)
