import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    try:
        img = Image.open(path)
        img.show()
        arr = np.array(img)
        print(arr)
        return arr
    except FileNotFoundError as msg:
        print(msg)


if __name__ == "__main__":
    print(ft_load('landscape.jpg'))
