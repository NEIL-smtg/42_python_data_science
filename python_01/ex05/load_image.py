import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    load img, print its data and return img array
    """
    try:
        img = Image.open(path)
        arr = np.array(img)
        print('The shape of image is: ', arr.shape)
        print(arr)
        return arr
    except FileNotFoundError:
        print('FileNotFoundError: Unable to open file ' + path)
