def get_max_rep_symbol(s: str) -> str:
    """
        Написать функцию, которая вычисляет символ, который идет
        подряд наибольшее кол-во раз.
        Например:
        assert get_max_rep_symbol("aaaabbccddddddef") == "d"
        assert get_max_rep_symbol("aaaabbaab") == "a"
        assert get_max_rep_symbol("aabb") == "a"
    """
    if not s:  # Обработка пустой строки
        return ""
    ls = []
    res = s[0]  # a

    for char in s[1:]:
        if char == res[0]:  # a
            res = res + char
        else:
            ls.append(res)
            res = char
    ls.append(res)
    ls.sort(key=lambda x: len(x), reverse=True)
    return ls[0][0]


if __name__ == "__main__":
    print(get_max_rep_symbol("aaaabbccddddddef"))
    print(get_max_rep_symbol("aaaabbaab"))
    print(get_max_rep_symbol("aabbb"))
