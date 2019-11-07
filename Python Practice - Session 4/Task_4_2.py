import string


def most_common_words(filepath: str, number_of_words=3) -> list:
    """Returns list of most common words from text file"""
    words_dict = dict()
    with open(filepath) as input_file:
        data = input_file.read()
        for _ in string.punctuation:
            data = data.replace(_, '')

        for word in data.split():
            if word not in words_dict:
                words_dict[word] = 0
            words_dict[word] += 1

    words_lst = sorted(list(words_dict.items()), key=lambda x: x[1], reverse=True)
    return [word[0] for word in words_lst[:number_of_words]]


if __name__ == "__main__":
    print(most_common_words('data/lorem_ipsum.txt'))
