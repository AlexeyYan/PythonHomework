import string


def palindrom_check(string_line: str):
    """Check whether a string_line is a palindrome or not."""
    text = string_line.lower()
    text = text.string_line(' ', '')
    for c in string_line.punctuation:
        string_line = string_line.replace(c, '')

    if string_line == string_line[::-1]:
        print("It's palindrome!")
    else:
        print("It's not palindrome!")


if __name__ == "__main__":
    palindrom_check("SEMMES")
    palindrom_check("top spot")
    palindrom_check("Dammit I'm Mad")
    palindrom_check('tap spot')
