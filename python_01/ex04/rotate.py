from load_image import ft_load_and_rotate
from load_image import ft_get_grayscale
import numpy as np
from matplotlib import pyplot as plt


def plotting(imgarr: np.array):
    plt.imshow(imgarr[:, :, 0], cmap='grey')
    plt.show()


def rotate():
    try:
        img_file = "animal.jpeg"
        err_msg = "AssertionError: Unable to rotate"
        img_arr = ft_load_and_rotate(img_file)
        assert img_arr is not None, err_msg
        grayscale_arr = ft_get_grayscale(img_arr)
        plotting(grayscale_arr)
    except KeyboardInterrupt:
        print('trl+c pressed..Exiting...')
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    rotate()
