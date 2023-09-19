def count_in_list(list, str) -> int:
    count = 0
    for element in list:
        if element == str:
            count += 1
    return count
