def combine_dicts(*args: dict) -> dict:
    """Returns combines given dictionaries them into one dictionary
       where values summarized in case of identical keys
    """
    summary_dict = {}
    for dct in args:
        for key in dct.keys():
            if key not in summary_dict:
                summary_dict[key] = 0
            summary_dict[key] += dct[key]
    return summary_dict


if __name__ == "__main__":
    dct1 = {'a': 100, 'b': 200}
    dct2 = {'a': 200, 'c': 300}
    dct3 = {'a': 300, 'd': 100}

    print(combine_dicts(dct1, dct2))
    print(combine_dicts(dct1, dct2, dct3))
