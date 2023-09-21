import numpy as np
from PIL import Image


def imgShow(array):
    """
    show the img
    """

    img = Image.fromarray(array)
    img.show()


def ft_invert(array) -> np.array:
    """Inverts the color of the image received
    """
    inv = np.invert(array)
    imgShow(inv)
    return inv


def ft_red(array) -> np.array:
    """Turns color of the image received into red
    setting the green and blue channel into 0
    """
    tinted_red = np.copy(array)
    tinted_red[:, :, 1] = 0
    tinted_red[:, :, 2] = 0
    imgShow(tinted_red)
    return tinted_red


def ft_green(array) -> np.array:
    """Turns color of the image received into grey
    setting the red and blue channel into 0
    """
    tinted_green = np.copy(array)
    tinted_green[:, :, 0] = 0
    tinted_green[:, :, 2] = 0
    imgShow(tinted_green)
    return tinted_green


def ft_blue(array) -> np.array:
    """Turns color of the image received into grey
    setting the red and green channel into 0
    """
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    imgShow(array)
    return array


def ft_grey(array) -> np.array:
    """Turns color of the image received into grey
    by multiplying rgb channel with luminance value
    respectively
    """
    grey = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
    imgShow(grey)
    return grey
