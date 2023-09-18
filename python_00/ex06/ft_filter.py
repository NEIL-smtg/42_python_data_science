import typing as ty


def even_or_odd(x):
    return "EVEN" if x % 2 == 0 else "ODD"


def bullshit():
    pass


def is_5(x):
    return x == 5


def is_even(x):
    return x % 2 == 0


T = ty.TypeVar('T')
R = ty.TypeVar('R')


def ft_filter(f: ty.Callable[[T], R], input: ty.Iterable[T]) -> list[T]:
    return [element for element in input if (f(element))]


if __name__ == "__main__":
    arr = [2, 4, 5, 6, 8, 10]
    res = list(filter(even_or_odd, arr))
    print(res)
    try:
        res = ft_filter(even_or_odd, arr)
        print(res)

        res = ft_filter(is_even, arr)
        print(res)

        res = ft_filter(is_5, arr)
        print(res)

        res = ft_filter(bullshit, arr)
        print(res)
    except TypeError:
        print("Error: Invalid function type")
