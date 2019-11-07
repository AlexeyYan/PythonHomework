def split_analog(text: str, sep=' ') -> list:
    """Separate string by sep"""
    lst = []
    temp_str = ''
    text += sep
    for ch in text:
        if ch != sep:
            temp_str += ch
        else:
            lst.append(temp_str)
            temp_str = ''
    return lst


if __name__ == "__main__":
    print(split_analog('eewr ewrw qd'))
    print(split_analog('wer-wer-wer -ewr', '-'))
