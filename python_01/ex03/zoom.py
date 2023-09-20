from load_image import ft_load
import numpy as np
from matplotlib import pyplot as plt


def plotImg(imgarr: np.array):
    plt.imshow(imgarr[:, :, 0], cmap='grey')
    plt.show()


def zoom(path: str):
    try:
        img_arr = ft_load(path)
        assert img_arr is not None, "Unable to zoom."

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

        print(grayscale_img)
        print("New shape after slicing: ", grayscale_img.shape)
        plotImg(grayscale_img)
    except AssertionError as msg:
        print(msg)
    except KeyboardInterrupt:
        print('trl+c pressed..Exiting...')


if __name__ == "__main__":
    zoom("animal.jpeg")
