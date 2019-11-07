import string


def test_1_1(*strings: list) -> set:
    """Returns characters that appear in all strings"""
    letters_set = set(strings[0])
    for s in strings:
        letters_set &= set(s)
    return letters_set


def test_1_2(*strings: list) -> set:
    """Returns characters that appear in at least one string"""
    letters_set = set(strings[0])
    for s in strings:
        letters_set |= set(s)
    return letters_set


def test_1_3(*strings: list) -> set:
    """Returns characters that appear at least in two strings"""
    letters_dict = {}
    for st in strings:
        for ch in st:
            if ch not in letters_dict:
                letters_dict[ch] = 0
            letters_dict[ch] += 1
    return {letter for letter in letters_dict if letters_dict[letter] > 1}


def test_1_4(*strings: list) -> set:
    """Returns characters of alphabet, that were not used in any string"""
    letters_set = set(string.ascii_lowercase)
    for s in strings:
        letters_set -= set(s)
    return letters_set


if __name__ == "__main__":
    print(test_1_1("hello", "world", "python"))
    print(test_1_2("hello", "world", "python"))
    print(test_1_3("hello", "world", "python"))
    print(test_1_4("hello", "world", "python"))
