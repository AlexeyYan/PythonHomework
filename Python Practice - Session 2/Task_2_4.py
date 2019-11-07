def split_by_indexes(s: str, indexes: list) -> list:
    """Splits the s string by indexes specified in indexes"""
    lst = []
    temp_str = ''
    indexes.append(len(s)-1)

    for index, ch in enumerate(list(s)):
        if index in indexes:
            lst.append(temp_str)
            temp_str = ''
        temp_str += ch
    lst[len(lst)-1] += temp_str

    return lst


if __name__ == "__main__":
    print(split_by_indexes("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
    print(split_by_indexes("myenglishverygood", [2, 9, 13, 21]))
    print(split_by_indexes("myenglishverygood", [100]))
