def get_pairs(lst):
    """Return a list of tuples containing pairs of elements."""
    if len(lst) <= 1:
        return None

    result_lst = []
    temp_lst = []

    for item in lst:
        if len(temp_lst) == 2:
            result_lst.append(tuple(temp_lst))
            temp_lst.pop(0)
        temp_lst.append(item)
    result_lst.append(tuple(temp_lst))
    return result_lst


if __name__ == "__main__":
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))
    print(get_pairs([1]))
    print(get_pairs([1, 2, 3]))
