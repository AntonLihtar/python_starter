def get_longest_common_prefix(words: list[str]) -> str:
    """
        Напишите функцию, которая в массиве слов ищет наиболее
        длинный общий префикс (начало слова).
        Например:
        get_longest_common_prefix(["flower", "flow", "flight"]) == "fl"
        Темы: списки, парсинг строк
    """

    if len(words) == 0:
        return ''

    main_str = words[0]
    result = ""
    for i, v in enumerate(main_str):
        for el in words:
            if i >= len(el) or el[i] != v:
                return result
        result += v
    return  result



if __name__ == "__main__":
    res = get_longest_common_prefix(["flower", "flow", "flight"])
    print(res)

    # "dairy products", "bakery", "drinks"
