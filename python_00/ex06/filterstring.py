import sys
import string


def ft_filterstring(strs, size):
    return [element for element in strs if len(element) > size]


if __name__ == "__main__":
    try:
        ac = len(sys.argv)
        assert ac != 2, "AssertionError: The arguments are bad."

        size = int(sys.argv[2])
        strs = sys.argv[1].split()

        assert any(ch in sys.argv[1] for ch in string.punctuation) is False,\
               "AssertionError: The arguments are bad."

        res = ft_filterstring(strs, size)
        if (res is None):
            print("[]")
        else:
            print(res)
    except AssertionError as msg:
        print(msg)
    except ValueError:
        print("ValueError: Second argument should be a int!")
