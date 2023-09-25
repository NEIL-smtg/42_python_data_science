import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    throw error when unable to open img
    otherwise return img data array
    """

    try:
        img = Image.open(path)
        arr = np.array(img)
        return arr
    except FileNotFoundError:
        print('FileNotFoundError: Unable to open ' + path)


# if __name__ == "__main__":
#     print(ft_load('.jpg'))
