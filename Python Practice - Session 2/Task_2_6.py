def get_shortest_word(s: str) -> str:
    """Return the longest word in the given string."""
    return min(s.split(), key=len)


if __name__ == "__main__":
    print(get_longest_word('Any pythonista like namespaces a lot.'))
    print(get_longest_word('aaaa bbbb cccc'))
    print(get_longest_word('Python is simple and effective!'))
