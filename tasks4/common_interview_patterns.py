# pylint: skip-file

def get_top_grade_students(all_students: dict[str, float]) -> dict[str, float]:
    """
        На входе подается словарь в формате "имя студента-средний балл".
        Словарь не обязательно упорядочен.
        Вернуть словарь, содержащий топ-3 студентов по среднему баллу
        Темы: словари
    """
    return {}


def contains_in_list(small: list[int], big: list[int]) -> bool:
    """
        Выведите true, если массив содержится в другом массиве
        в том же порядке. Не обязательно элементы должны идти один
        за другим.

        contains_in_list([3, 4, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == true
        Темы: списки
    """
    return True


def get_most_frequent_symbol(s: str) -> tuple[str, int]:
    """
        Вернуть символ (и число символов), который встречается в строке чаще всего независимо
        от порядка. Например:
        get_most_frequent_symbol("aaeeaeabenbdedeeeddaaadffeffseee") == (e, 12)
        Темы: парсинг строк, словарь
    """
    return "", 0


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
    return False


def get_max_rep_symbol(s: str) -> str:
    """
        Написать функцию, которая вычисляет символ, который идет
        подряд наибольшее кол-во раз.
        Например:
        assert get_max_rep_symbol("aaaabbccddddddef") == "d"
        assert get_max_rep_symbol("aaaabbaab") == "a"
        assert get_max_rep_symbol("aabb") == "a"
    """
    return ""


def get_longest_common_prefix(words: list[str]) -> str:
    """
        Напишите функцию, которая в массиве слов ищет наиболее
        длинный общий префикс (начало слова).
        Например:
        get_longest_common_prefix(["flower", "flow", "flight"]) == "fl"
        Темы: списки, парсинг строк
    """
    return ""


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
    return False


def reverse_words(input_str: str) -> str:
    """
        Написать функцию, которая принимает предложение и возвращает
        строка со словами из исходного предложения в обратном порядке.
        actual = reverse_words("the sky is blue") == "blue is sky the"
        Темы: парсинг строк
    """
    return ""
