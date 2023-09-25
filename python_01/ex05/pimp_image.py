import numpy as np
from PIL import Image


def imgShow(array):
    """show the img"""

    img = Image.fromarray(array)
    img.show()


def ft_invert(array) -> np.array:
    """Inverts the color of the image received"""

    try:
        if array is None:
            raise AssertionError('Error : Unable to generate ImgArray')
        inv = 255 - array
        imgShow(inv)
        return inv
    except AssertionError as msg:
        print(msg)


def ft_red(array) -> np.array:
    """Turns color of the image received into red"""

    try:
        if array is None:
            raise AssertionError('Error : Unable to generate ImgArray')
        tinted_red = np.copy(array)
        tinted_red[:, :, 1] = 0
        tinted_red[:, :, 2] = 0
        imgShow(tinted_red)
        return tinted_red
    except AssertionError as msg:
        print(msg)


def ft_green(array) -> np.array:
    """Turns color of the image received into green"""

    try:
        if array is None:
            raise AssertionError('Error : Unable to generate ImgArray')
        tinted_green = np.copy(array)
        tinted_green[:, :, 0] = 0
        tinted_green[:, :, 2] = 0
        imgShow(tinted_green)
        return tinted_green
    except AssertionError as msg:
        print(msg)


def ft_blue(array) -> np.array:
    """Turns color of the image received into blue"""

    try:
        if array is None:
            raise AssertionError('Error : Unable to generate ImgArray')
        array[:, :, 0] = 0
        array[:, :, 1] = 0
        imgShow(array)
        return array
    except AssertionError as msg:
        print(msg)


def ft_grey(array) -> np.array:
    """Turns color of the image received into grey"""

    try:
        if array is None:
            raise AssertionError('Error : Unable to generate ImgArray')
        mean = np.mean(array, axis=2, keepdims=True)
        grey = np.repeat(mean, 3, axis=2)

        imgShow(np.array(grey, dtype=np.uint8))
        return grey
    except AssertionError as msg:
        print(msg)
