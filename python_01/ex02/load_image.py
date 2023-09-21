import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    throw error when unable to open img
    otherwise return img data array
    """

    try:
        img = Image.open(path)
        img.show()
        arr = np.array(img)
        print(arr)
        return arr
    except FileNotFoundError as msg:
        print(msg)


if __name__ == "__main__":
    print(ft_load('landscape.jpg'))
