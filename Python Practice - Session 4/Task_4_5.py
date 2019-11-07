def remember_result(func):
    """Remembers last result of function it decorates
       and prints it before next call.
    """
    prev_result = 'None'

    def wrapper(*args, **kwargs):
        nonlocal prev_result
        print(f"Last result = '{prev_result}'")
        prev_result = func(*args, **kwargs)
        return prev_result
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


sum_list("a", "b")
sum_list("abc", "cde")
# sum_list(3, 4, 5)
