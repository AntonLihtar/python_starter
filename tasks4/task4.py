def are_brackets_correct(s: str) -> bool:
    """
        Напишите функцию, которая возвращает true, если скобочная последовательность
        является правильной, т.е. все открывающиеся скобки соответствуют закрывающимся.
        Скобки могут быть круглыми и квадратными.
        ((( ))) - правильно.
        [][][] - правильно
        [()][] - правильно
        [(][)] - неправильно
        Темы: парсинг строк, стек (stack)
    """
    if len(s) < 2:
        return False

    scope = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    res = []

    for char in s:
        if char == " " or char.isalpha():
            continue
        if char in scope:
            res.append(scope[char])
        else:
            if len(res) > 0:
                end_char = res.pop()
                if end_char == char:
                    continue
                else:
                    return False
            else:
                return False
    return len(res) == 0


if __name__ == "__main__":
    print(are_brackets_correct('([](( ) )[{}])'))
    print(are_brackets_correct('a(b)c'))

