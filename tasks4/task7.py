def has_black_list_words(input_str: str, black_list: list[str]) -> bool:
    """
        Дана строка и стоп-лист стоп-слов.
        Напишите функцию, которая возвращает true, если в строке
        есть хотя бы одно слово из стоп-листа.
        Разумеется, функция должна работать даже если есть знаки препинания.
        Темы: списки, парсинг строк
        Например:
        assert has_black_list_words("А попа была собака, он ее любил", [
                                "собака", "кот", "мышь"])
    """
    result = ''
    for s in input_str:
        if s.isalpha() or s.isspace():
            result += s
    result = result.split()

    for el in result:
        if el.lower() in black_list:
            return True
    return False


if __name__ == "__main__":
    res = has_black_list_words("У попа была собака, он ее любил", [
        "собака", "кот", "мышь"])
    print(res)
