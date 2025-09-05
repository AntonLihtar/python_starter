import pytest
from tasks4.task1 import get_top_grade_students
from tasks4.task2 import contains_in_list
from tasks4.task3 import get_most_frequent_symbol
from tasks4.task4 import are_brackets_correct
from tasks4.task5 import get_max_rep_symbol
from tasks4.task6 import get_longest_common_prefix
from tasks4.task7 import has_black_list_words
# from tasks4.task8 import has_black_list_words


def test_get_top_grade_students():
    # Тест 1: обычный случай — более 3 студентов с разными баллами
    students = {
        "Анна": 4.5,
        "Борис": 4.8,
        "Виктор": 4.2,
        "Галина": 4.9,
        "Дмитрий": 4.1
    }
    result = get_top_grade_students(students)
    expected = {"Галина": 4.9, "Борис": 4.8, "Анна": 4.5}
    assert result == expected, f"Ожидалось {expected}, получено {result}"

    # Тест 2: одинаковые баллы — должны попасть все с максимальными значениями (до 3)
    students = {
        "Елена": 4.7,
        "Фёдор": 4.7,
        "Катя": 4.7,
        "Лёва": 4.0
    }
    result = get_top_grade_students(students)
    expected_keys = ["Елена", "Фёдор", "Катя"]  # Все с 4.7, порядок может сохраниться как в sorted
    expected = dict(zip(expected_keys, [4.7, 4.7, 4.7]))
    assert list(result.keys()) == expected_keys
    assert list(result.values()) == [4.7, 4.7, 4.7]

    # Тест 3: меньше 3 студентов — возвращаются все, в порядке убывания
    students = {
        "Маша": 4.6,
        "Петя": 4.9
    }
    result = get_top_grade_students(students)
    expected = {"Петя": 4.9, "Маша": 4.6}
    assert result == expected, f"Ожидалось {expected}, получено {result}"

    # Тест 4: только один студент
    students = {"Оля": 5.0}
    result = get_top_grade_students(students)
    expected = {"Оля": 5.0}
    assert result == expected, f"Ожидалось {expected}, получено {result}"

    # Тест 5: пустой словарь — должен вернуть пустой словарь
    students = {}
    result = get_top_grade_students(students)
    expected = {}
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_contains_in_list():
    # Тест 1: обычный случай - подсписок содержится в правильном порядке
    assert contains_in_list([3, 4, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True

    # Тест 2: элементы в неправильном порядке
    assert contains_in_list([8, 4, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False

    # Тест 3: пустой маленький список
    assert contains_in_list([], [1, 2, 3]) == True

    # Тест 4: оба списка пустые
    assert contains_in_list([], []) == True

    # Тест 5: маленький список длиннее большого
    assert contains_in_list([1, 2, 3], []) == False

    # Тест 6: точное совпадение списков
    assert contains_in_list([1, 2, 3], [1, 2, 3]) == True

    # Тест 7: элементы есть, но не в том порядке
    assert contains_in_list([3, 1], [1, 2, 3]) == False

    # Тест 8: повторяющиеся элементы в правильном порядке
    assert contains_in_list([1, 2, 1], [1, 3, 2, 1]) == True

    # Тест 9: повторяющиеся элементы в неправильном порядке
    assert contains_in_list([1, 2, 1], [1, 2, 2, 1]) == True

    # Тест 10: элемент отсутствует
    assert contains_in_list([1, 5], [1, 2, 3]) == False

    # Тест 11: большой список, но подсписок в конце
    assert contains_in_list([8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True

    # Тест 12: подсписок в начале
    assert contains_in_list([1, 2], [1, 2, 3, 4, 5]) == True

    # Тест 13: один элемент найден
    assert contains_in_list([5], [1, 2, 3, 4, 5, 6]) == True

    # Тест 14: один элемент не найден
    assert contains_in_list([7], [1, 2, 3, 4, 5, 6]) == False

    # Тест 15: сложный случай с повторениями
    assert contains_in_list([1, 3, 1], [1, 2, 3, 1, 2, 3, 1]) == True

    # Тест 16: первый элемент на позиции 0
    assert contains_in_list([1, 3], [1, 2, 3, 4]) == True

    # Тест 17: подсписок не найден из-за порядка
    assert contains_in_list([2, 1], [1, 2, 3]) == False

    # Тест 18: все элементы одинаковые
    assert contains_in_list([2, 2], [1, 2, 2, 3]) == True

    # Тест 19: все элементы одинаковые, но не хватает
    assert contains_in_list([2, 2, 2], [1, 2, 2, 3]) == False

    # Тест 20: большой список, подсписок в середине
    assert contains_in_list([4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]) == True


def test_run_get_most_frequent_symbol():
    # Тест 1: Пример из условия
    assert get_most_frequent_symbol("aaeeaeabenbdedeeeddaaadffeffseee") == ('e', 12), \
        "Тест 1 не пройден: ожидается ('e', 12)"

    # Тест 2: Пустая строка
    assert get_most_frequent_symbol("") == ('', 0), \
        "Тест 2 не пройден: пустая строка должна давать ('', 0)"

    # Тест 3: Один символ
    assert get_most_frequent_symbol("a") == ('a', 1), \
        "Тест 3 не пройден: один символ"

    # Тест 4: Все символы одинаковые
    assert get_most_frequent_symbol("aaaaaa") == ('a', 6), \
        "Тест 4 не пройден: все символы одинаковые"

    # Тест 5: Равное количество (выбирается первый по порядку в Counter)
    assert get_most_frequent_symbol("aabbcc") == ('a', 2), \
        "Тест 5 не пройден: при равенстве — выбирается первый встретившийся"

    # Тест 6: Разные символы, один явно чаще
    assert get_most_frequent_symbol("abccc") == ('c', 3), \
        "Тест 6 не пройден: 'c' встречается чаще"

    # Тест 7: Пробелы и символы
    assert get_most_frequent_symbol("hello world") == ('l', 3), \
        "Тест 7 не пройден: 'l' встречается 3 раза"


def test_are_brackets_correct():
    # Правильные последовательности
    assert are_brackets_correct("()") == True
    assert are_brackets_correct("(())") == True
    assert are_brackets_correct("[][]") == True
    assert are_brackets_correct("{{}}") == True
    assert are_brackets_correct("()[]{}") == True
    assert are_brackets_correct("([{}])") == True
    assert are_brackets_correct("()[][]{{}}") == True
    assert are_brackets_correct("[]}") == False
    assert are_brackets_correct("([)]") == False
    assert are_brackets_correct(" ") == False  # только пробелы
    assert are_brackets_correct("a(b)c") == True
    assert are_brackets_correct("a(b]c") == False

def test_get_max_rep_symbol():
    assert get_max_rep_symbol("aaaabbccddddddef") == "d"
    assert get_max_rep_symbol("aaaabbaab") == "a"
    assert get_max_rep_symbol("aabb") == "a"
    assert get_max_rep_symbol("aabbb") == "b"
    assert get_max_rep_symbol("abcdef") == "a"  # все по 1, первый
    assert get_max_rep_symbol("") == ""  # пустая строка
    assert get_max_rep_symbol("a") == "a"  # один символ
    assert get_max_rep_symbol("aaaa") == "a"  # все одинаковые
    assert get_max_rep_symbol("bbbaaa") == "b"  # первая последовательность длиннее

def test_get_longest_common_prefix():
    assert get_longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert get_longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert get_longest_common_prefix(["interspecies", "interstellar", "interstate"]) == "inters"
    assert get_longest_common_prefix([""]) == ""
    assert get_longest_common_prefix([]) == ""
    assert get_longest_common_prefix(["single"]) == "single"
    assert get_longest_common_prefix(["same", "same", "same"]) == "same"
    assert get_longest_common_prefix(["abc", "ab", "abcd"]) == "ab"  # "ab" - общий префикс
    assert get_longest_common_prefix(["prefix", "preform", "prepare"]) == "pre"
    assert get_longest_common_prefix(["a"]) == "a"


def test_has_black_list_words():
    # Тест 1: базовый случай - слово найдено
    assert has_black_list_words("А попа была собака, он ее любил", ["собака", "кот", "мышь"]) == True

    # Тест 2: слово не найдено
    assert has_black_list_words("У меня есть кошка", ["собака", "кот", "мышь"]) == False

    # Тест 3: регистр не важен
    assert has_black_list_words("СОБАКА бегает по двору", ["собака"]) == True
    assert has_black_list_words("У меня есть Кот", ["кот"]) == True
    assert has_black_list_words("МЫШЬ в доме", ["мышь"]) == True

    # Тест 4: знаки препинания
    assert has_black_list_words("Собака! Какая красивая.", ["собака"]) == True
    assert has_black_list_words("Мой кот, он замечательный", ["кот"]) == True
    assert has_black_list_words("Это мышь? Да, это мышь!", ["мышь"]) == True

    # Тест 5: частичное совпадение (не должно срабатывать)
    assert has_black_list_words("собачка", ["собака"]) == False
    assert has_black_list_words("котенок", ["кот"]) == False
    assert has_black_list_words("мышиный", ["мышь"]) == False

    # Тест 6: пустая строка
    assert has_black_list_words("", ["собака"]) == False

    # Тест 7: пустой стоп-лист
    assert has_black_list_words("любое слово", []) == False

    # Тест 8: оба списка пустые
    assert has_black_list_words("", []) == False

    # Тест 9: несколько слов из стоп-листа
    assert has_black_list_words("У меня есть собака и кот", ["собака", "кот", "мышь"]) == True

    # Тест 10: слова с цифрами
    assert has_black_list_words("У меня кот2021", ["кот"]) == True
    assert has_black_list_words("Собака345 стоит здесь", ["собака"]) == True

    # Тест 11: сложная пунктуация
    assert has_black_list_words("Привет, кот! Как дела?", ["кот"]) == True
    assert has_black_list_words("Смотри: это собака; она милая", ["собака"]) == True

    # Тест 12: слово в середине предложения
    assert has_black_list_words("Я вчера видел мышь в доме", ["мышь"]) == True

    # Тест 13: множественные пробелы и знаки
    assert has_black_list_words("Собака   !   @  #  $  %  ^  &  *  (  )  _  +", ["собака"]) == True

    # Тест 14: слово из нескольких стоп-слов
    assert has_black_list_words("У меня есть кот", ["собака", "кот", "мышь"]) == True

    # Тест 15: похожие слова но не совпадающие
    assert has_black_list_words("собачий", ["собака"]) == False
    assert has_black_list_words("кошачий", ["кот"]) == False