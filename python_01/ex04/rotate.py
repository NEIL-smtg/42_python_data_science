from load_image import ft_load
import numpy as np
from matplotlib import pyplot as plt


def plotting(imgarr: np.array):
    """0 to specify using column 0 of color axis
    changing color mapping into gray to achieve
    grayscale effect"""

    plt.imshow(imgarr[:, :, 0:], cmap='gray')
    plt.show()


def crop(img_arr: np.array) -> np.array:
    """crop img into 400x400 and apply offset to move the
    cropping area into rocket's head"""

    height = len(img_arr[0])
    width = len(img_arr[1])

    mid_h = height // 2
    mid_w = width // 2

    offset_x = 150
    offset_y = -220

    left = mid_w - 200 + offset_x
    right = mid_w + 200 + offset_x
    top = mid_h - 200 + offset_y
    bottom = mid_h + 200 + offset_y

    crop_img = img_arr[top:bottom, left:right, :3]
    res = np.mean(crop_img, axis=2, keepdims=True).astype(np.uint8)
    print(f'The shape of the image is: {res.shape}')
    print(res)
    return res


def transpose(img_arr: np.array) -> np.array:
    """tranposingg"""
    rows, cols, channels = img_arr.shape
    tr = np.empty((cols, rows, channels), dtype=img_arr.dtype)

    for i in range(rows):
        for j in range(cols):
            tr[j][i] = img_arr[i][j]
    print(f'New shape after transpose: {tr.shape[0], tr.shape[1]}')
    print(tr[:, :, 0])
    return tr


def rotate():
    """throw error when img not loaded
    transpose, get grayscale arr and plot"""

    try:
        img_file = "animal.jpeg"
        err_msg = "AssertionError: Unable to rotate"
        img_arr = ft_load(img_file)
        assert img_arr is not None, err_msg

        crop_img = crop(img_arr)
        tr = transpose(crop_img)
        plotting(tr)

    except KeyboardInterrupt:
        print('\nCtrl+c pressed..Exiting...')
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    rotate()
