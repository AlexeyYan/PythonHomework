def foo(lst: list) -> list:
    """Return a new list such that each element at index i of the new list
       is the product of all the numbers in the original array except the one at i
    """
    new_list = []

    for index in range(len(lst)):
        value = 1
        for num in (lst[:index]+lst[index+1:]):
            value *= num
        new_list.append(value)

    return new_list


if __name__ == "__main__":
    print(foo([1, 2, 3, 4, 5]))
    print(foo([3, 2, 1]))
    print(foo([4, 6, 7, 2]))
