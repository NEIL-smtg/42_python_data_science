def get_mean(lst: list) -> float:
    """calc mean"""
    return (sum([float(n) for n in lst]) / len(lst))


def get_median(lst: list) -> [int | float]:
    """calc median"""
    lst.sort()
    mid = len(lst) // 2
    return lst[mid]


def get_quartile(lst: list) -> list:
    """calc quatile [0.25, 0.75]"""
    lst.sort()
    idx1 = len(lst) // 4
    idx2 = len(lst) * 3 // 4
    return [lst[idx1], lst[idx2]]


def get_variance(lst: list) -> float:
    """calc variance"""
    mean = get_mean(lst)
    res = sum([pow((x - mean), 2) for x in lst])
    res /= len(lst)
    return res


def get_std(lst: list) -> float:
    """calc standard deviation, just sqrt(var)"""
    return pow(get_variance(lst), 0.5)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """if args empty or not number, throw error
    if keyword arg is not in valid_param, print error
    otherwise print calculated value"""
    try:
        err = 'ERROR'
        assert kwargs, err
        assert all(type(x) in (float, int) for x in args), err

        valid_param = ['mean', 'median', 'quartile', 'std', 'var']
        lst = list(args)

        for val in kwargs.values():
            if val not in valid_param:
                return
            if len(args) == 0:
                print(err)
            elif val == 'mean':
                print('mean :', get_mean(lst))
            elif val == 'median':
                print('median =', get_median(lst))
            elif val == 'quartile':
                print('quartile :', get_quartile(lst))
            elif val == 'std':
                print('std :', get_std(lst))
            else:
                print('var :', get_variance(lst))

    except AssertionError as msg:
        print(msg)
        return
