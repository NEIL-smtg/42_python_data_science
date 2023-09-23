def square(x: int | float) -> int | float:
    """return squared of number"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """return exponential of number itself"""
    return x ** x


def outer(x: int | float, function) -> object:
    """remain the state of this function no
    no matter how many times this func get called,
    the inner can be see as another call to this function"""
    count = 0
    _x = x

    def inner() -> float:
        """count is not local var of inner func,
        keep overwriting the value by calling the func
        so the value of variable remains"""
        nonlocal count
        count += 1
        res = _x
        for _ in range(count):
            res = function(res)
        return (res)

    return inner
