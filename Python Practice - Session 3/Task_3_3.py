def count_letters(string: str) -> dict:
    """Returns a dictionary, that contains letters of given string
       as keys and a number of their occurrence as values.
    """
    letters_dict = {}
    for letter in string:
        if letter not in letters_dict:
            letters_dict[letter] = 0
        letters_dict[letter] += 1
    return letters_dict


if __name__ == "__main__":
    print(count_letters('aabbbbcccd'))
    print(count_letters('stringsample'))
