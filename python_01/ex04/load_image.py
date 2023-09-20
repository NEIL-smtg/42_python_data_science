import numpy as np
from PIL import Image


def ft_get_grayscale(img_arr: np.array) -> np.array:
    height = len(img_arr)
    width = len(img_arr[1])

    mid_h = height // 2
    mid_w = width // 2

    offset_x = -100
    offset_y = -140

    left = mid_w - 200 + offset_x
    right = mid_w + 200 + offset_x
    top = mid_h - 200 + offset_y
    bottom = mid_h + 200 + offset_y

    crop_img = img_arr[top:bottom, left:right, :3]

    grayscale_img = np.mean(crop_img, axis=2, keepdims=True)\
        .astype(np.uint8)
    return grayscale_img


def ft_load_and_rotate(path: str) -> np.array:
    try:
        img = Image.open(path)
        print(np.array(img).shape)
        rotated = img.rotate(90)
        arr = np.array(rotated)
        return arr
    except FileNotFoundError as msg:
        print(msg)


# if __name__ == "__main__":
#     print(ft_load('.jpg'))
