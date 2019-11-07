def generate_squares(num: int) -> dict:
    """Returns a dictionary, where the key is a number
       and the value is the square of that number.
    """
    return {x: x*x for x in range(1, num+1)}


if __name__ == "__main__":
    print(generate_squares(5))
    print(generate_squares(7))
