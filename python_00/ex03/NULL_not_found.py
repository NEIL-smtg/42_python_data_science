
# when a num = NAN, u can use num != num to compare
# only valid in python

def NULL_not_found(object: any) -> int:
    if (object is None):
        print('Nothing', ':', object, type(object))
    elif type(object) is float and object != object:
        print('Cheese:', object, float)
    elif type(object) is int:
        print('Zero:', object, int)
    elif (type(object) is str and object == ''):
        print('Empty:', str)
    elif (type(object) is bool):
        print('Fake:', object, bool)
    else:
        print('Type not found')
        return 1
    return 0
