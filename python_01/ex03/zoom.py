from load_image import ft_load
import numpy as np
from matplotlib import pyplot as plt


def plotImg(imgarr: np.array):
    """show the image using imshow
    0 is to specify using column 0 in that dimension for color
    cmap = color map, its default color mapping is viridis
    change it to gray to apply grayscale effect"""

    plt.imshow(imgarr[:, :, 0], cmap='gray')
    plt.show()


def zoom():
    """Throw error when unable to open img
    -mid_h, mid_w to find the center coordinate of the img
     then calculate top left, right, bottom left right
    -by adding and subtracting 200 to achieve 400x400 img scale
    -offset xy is to move the cropping area to aim at rocket's head
    -using axis 2 of the image array to find the mean of rgb values
    and trim 3 columns into 1 just to store 1 value for grayscale and
    setting the type to uint8 (0-255) in case the result will be in
    decimal point"""

    try:
        path = "animal.jpeg"
        img_arr = ft_load(path)
        if img_arr is None:
            raise AssertionError('Unable to zoom.')

        print("The shape of image is: ", img_arr.shape)
        print(img_arr)
        height = len(img_arr)
        width = len(img_arr[1])

        mid_h = height // 2
        mid_w = width // 2

        offset_x = 120
        offset_y = -80

        left = mid_w - 200 + offset_x
        right = mid_w + 200 + offset_x
        top = mid_h - 200 + offset_y
        bottom = mid_h + 200 + offset_y

        crop_img = img_arr[top:bottom, left:right, :3]

        grayscale_img = np.mean(crop_img, axis=2, keepdims=True)\
            .astype(np.uint8)

        print("New shape after slicing: ", grayscale_img.shape)
        print(grayscale_img)
        plotImg(grayscale_img)
    except AssertionError as msg:
        print(msg)
    except KeyboardInterrupt:
        print('\nCtrl+c pressed..Exiting...')


if __name__ == "__main__":
    zoom()
