def get_digits(num: int) -> tuple:
    """Return a tuple of a given integer's digits."""
    temp_lst = [int(digit) for digit in str(num)]
    return tuple(temp_lst)


if __name__ == "__main__":
    print(get_digits(12345678))
    print(get_digits(4253634534534))
