# def even_or_odd(x):
#     return "EVEN" if x % 2 == 0 else "ODD"


# def bullshit():
#     pass


# def is_5(x):
#     return x == 5


# def is_even(x):
#     return x % 2 == 0


def ft_filter(function, iterable) -> list:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return (element for element in iterable if element)
    return (element for element in iterable if (function(element)))


# if __name__ == "__main__":
#     arr = [2, 4, 5, 6, 8, 10]
#     try:
#         res = list(ft_filter(even_or_odd, arr))
#         print(res)

#         res = list(ft_filter(is_even, arr))
#         print(res)

#         res = list(ft_filter(is_5, arr))
#         print(res)

#         res = list(ft_filter(bullshit, arr))
#         print(res)
#     except TypeError:
#         print("Error: Invalid function type")
