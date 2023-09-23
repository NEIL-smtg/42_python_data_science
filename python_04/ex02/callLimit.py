def callLimit(limit: int):
    """call limit base func, setting count = 0"""
    count = 0

    def callLimiter(function):
        """callLimiter (first inner) : return inner2"""

        def limit_function(*args: any, **kwds: any):
            """add count if count < limit, print error otherwise"""
            nonlocal count
            if (count < limit):
                count += 1
                function(*args, **kwds)
            else:
                print(f'Error: {function} call too many times')

        return limit_function

    return callLimiter
