def all_thing_is_obj(object: any) -> int:
    obj_type = (list, tuple, set, dict, str)

    if type(object) not in obj_type:
        print('Type not found')
    elif type(object) is str:
        print(object, 'is in the kitchen :', str)
    elif type(object) is list:
        print('List :', list)
    elif type(object) is tuple:
        print('Tuple :', tuple)
    elif type(object) is set:
        print('Set :', set)
    else:
        print('Dict :', dict)
    return 42
