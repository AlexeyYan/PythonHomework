def call_once(func):
    """Runs a  decorated function or method once."""
    was_called = False

    def wrapper(*args, **kwargs):
        nonlocal was_called
        if not was_called:
            was_called = True
            return func(*args, **kwargs)
        else:
            return None
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


if __name__ == "__main__":
    print(sum_of_numbers(12, 4))
    print(sum_of_numbers(4, 6))
    print(sum_of_numbers(34, 1))
