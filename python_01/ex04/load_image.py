import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """load image and rotate 90 degrees to achieve
    transpose img and return the image array"""

    try:
        img = Image.open(path)
        arr = np.array(img)
        return arr
    except FileNotFoundError:
        print('FileNotFoundError: Unable to open ' + path)


# if __name__ == "__main__":
#     print(ft_load('.jpg'))
