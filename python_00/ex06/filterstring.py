import sys
import ft_filter as fl


if __name__ == "__main__":
    """
    lambda = function that has no name
    throw error when argument is invalid
    filter the arguments by checking strlen of argv
    """
    try:
        ac = len(sys.argv)
        assert ac == 3, "AssertionError: The arguments are bad."

        size = int(sys.argv[2])
        strs = sys.argv[1].split()

        for ch in sys.argv[1]:
            assert ch.isprintable() and (ch.isalnum() or ch.isspace()), \
                "AssertionError: The arguments are bad."

        res = list(fl.ft_filter(lambda element: len(element) > size, strs))
        if (res is None):
            print("[]")
        else:
            print(res)
    except AssertionError as msg:
        print(msg)
    except ValueError:
        print("ValueError: Second argument should be a int!")
