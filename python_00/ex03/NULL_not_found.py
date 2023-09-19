
# when a num = NAN, u can use num != num to compare
# only valid in python

def NULL_not_found(object: any) -> int:
    if (object is None):
        print('Nothing: none', type(object))
    elif (object is False):
        print('Fake: false', type(object))
    elif (isinstance(object, float) and object != object):
        print('Cheese: nan', type(object))
    elif (isinstance(object, int) and object == 0):
        print('Zero: 0', type(object))
    elif (isinstance(object, str) and object == ''):
        print('Empty: ', type(object))
    else:
        print("Type not found")
        return 1
    return 0
