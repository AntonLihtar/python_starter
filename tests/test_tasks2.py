import pytest
from tasks2.task1 import get_views_count
from tasks2.task2 import move_zeros, move_zeros2, move_zeros_v2
from tasks2.task3 import clean_name, is_rus_char
from tasks2.task4 import get_pct_growth



def test_task1():
    assert get_views_count(1) == "1 просмотр"
    assert get_views_count(4) == "4 просмотра"
    assert get_views_count(7) == "7 просмотров"
    assert get_views_count(0) == "0 просмотров"
    assert get_views_count(1000) == "1000 просмотров"
    # Проверка исключений
    with pytest.raises(ValueError):
        get_views_count(-11)

    with pytest.raises(ValueError, match="n не может быть отрицательным"):
        get_views_count(-2)


def test_move_zeros():
    # Базовый тест
    assert move_zeros([1, 0, 0, 2, 3, 0, 1]) == [1, 2, 3, 1, 0, 0, 0]
    # Пустой список
    assert move_zeros([]) == []
    # Без нулей
    assert move_zeros([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    # Все нули
    assert move_zeros([0, 0, 0, 0]) == [0, 0, 0, 0]
    # Один ноль
    assert move_zeros([1, 0, 2]) == [1, 2, 0]
    # Один элемент - ноль
    assert move_zeros([0]) == [0]
    # Один элемент - не ноль
    assert move_zeros([5]) == [5]
    # Отрицательные числа
    assert move_zeros([-1, 0, -2, 0, 3]) == [-1, -2, 3, 0, 0]
    # Числа с плавающей точкой
    assert move_zeros([1.5, 0.0, 2.7, 0, 3.14]) == [1.5, 2.7, 3.14, 0.0, 0]
    # Проверка, что оригинальный список не изменяется
    original = [1, 0, 2, 0, 3]
    original_copy = original.copy()
    result = move_zeros(original)
    assert original == original_copy  # Оригинал не должен измениться
    assert result == [1, 2, 3, 0, 0]


def test_move_zeros2():
    # Тесты для функции move_zeros2 (изменяет исходный список)
    # Базовый тест
    lst = [1, 0, 0, 2, 3, 0, 1]
    move_zeros2(lst)
    assert lst == [1, 2, 3, 1, 0, 0, 0]
    # Пустой список
    lst = []
    move_zeros2(lst)
    assert lst == []
    # Без нулей
    lst = [1, 2, 3, 4, 5]
    move_zeros2(lst)
    assert lst == [1, 2, 3, 4, 5]
    # Все нули
    lst = [0, 0, 0, 0]
    move_zeros2(lst)
    assert lst == [0, 0, 0, 0]
    # Проверка, что функция возвращает None
    lst = [1, 0, 2]
    result = move_zeros2(lst)
    assert result is None


def test_move_zeros_v2():
    # Базовый тест
    assert move_zeros_v2([1, 0, 0, 2, 3, 0, 1]) == [1, 2, 3, 1, 0, 0, 0]
    # Пустой список
    assert move_zeros_v2([]) == []
    # Без нулей
    assert move_zeros_v2([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    # Все нули
    assert move_zeros_v2([0, 0, 0, 0]) == [0, 0, 0, 0]
    # Один ноль
    assert move_zeros_v2([1, 0, 2]) == [1, 2, 0]
    # Один элемент
    assert move_zeros_v2([0]) == [0]
    assert move_zeros_v2([5]) == [5]


def test_clean_name():
    # Базовый тест
    assert clean_name("Иsвtrан/ов Ив^%ан Ива?но)вич") == "Иванов Иван Иванович"
    # Пустая строка
    assert clean_name("") == ""
    # Только русские буквы и пробелы
    assert clean_name("Иванов Иван Иванович") == "Иванов Иван Иванович"
    # Только латинские буквы и символы
    assert clean_name("abc def ghi") == "  "  # только пробелы остаются
    # Только специальные символы
    assert clean_name("!@#$%^&*()") == ""
    # Смешанные символы
    assert clean_name("И1в2а3н4о5в") == "Иванов"
    # Заглавные русские буквы
    assert clean_name("ИВАНОВ") == "ИВАНОВ"
    # Пробелы в начале и конце
    assert clean_name("  Иван  ") == "  Иван  "
    # # Множественные пробелы
    assert clean_name("Иван   Петров") == "Иван   Петров"
    # Дефисы (не русские буквы)
    assert clean_name("Иван-Петров") == "ИванПетров"
    # Цифры
    assert clean_name("Иван123Петров") == "ИванПетров"
    # Подчеркивания
    assert clean_name("Иван_Петров") == "ИванПетров"
    # Скобки
    assert clean_name("Иван(Петров)") == "ИванПетров"
    # Точки
    assert clean_name("И.П.Иванов") == "ИПИванов"
    # # Разные языки
    assert clean_name("ИванIvanИван") == "ИванИван"
    # Ё буква (в вашей функции её нет, поэтому она удалится)
    assert clean_name("Ёжик") == "Ёжик"
    # Все буквы русского алфавита (в нижнем регистре)
    assert clean_name("абвгдежзийклмнопрстуфхцчшщъыьэюя") == "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    # Все буквы русского алфавита (в верхнем регистре)
    assert clean_name("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ") == "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    # Сложный случай с множеством мусора
    assert clean_name("А!л@е#к$с%е^й&*()_+й-=QWERTYйцукен") == "Алексейййцукен"


def test_is_rus_char():
    """Тесты для функции is_rus_char"""
    # Русские буквы в нижнем регистре
    russian_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    for char in russian_lower:
        assert is_rus_char(char) == True
    # Русские буквы в верхнем регистре
    russian_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    for char in russian_upper:
        assert is_rus_char(char) == True
    # Латинские буквы
    latin_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in latin_chars:
        assert is_rus_char(char) == False
    # Цифры
    digits = "0123456789"
    for char in digits:
        assert is_rus_char(char) == False
    # Специальные символы
    special_chars = " !@#$%^&*()_+-=[]{}|;':\",./<>?"
    for char in special_chars:
        assert is_rus_char(char) == False


def test_get_pct_growth():
    # Базовый тест
    result = get_pct_growth([100, 150, 75, 120])
    assert result == [None, 50, -50, 60]
    # Один элемент
    assert get_pct_growth([100]) == [None]
    # Пустой список
    assert get_pct_growth([]) == []
    # Два элемента - рост
    assert get_pct_growth([100, 120]) == [None, 20]
    # Два элемента - падение
    assert get_pct_growth([100, 80]) == [None, -20]
    # Нулевые значения
    assert get_pct_growth([0, 100]) == [None, None]  # Деление на 0 -> None в результате
    # Отрицательные значения
    assert get_pct_growth([-100, -50]) == [None, -50]  # -50 / -100 * 100 - 100 = -50
    # Дробные значения
    result = get_pct_growth([10, 15, 7.5])
    expected = [None, 50, -50]
    assert result == expected


def test_get_pct_growth2():
    # Базовый тест
    result = get_pct_growth([100, 150, 75, 120])
    expected = [None, 50, -50, 60]
    assert result == expected

    # Один элемент
    assert get_pct_growth([100]) == [None]
    # Пустой список
    assert get_pct_growth([]) == []
    # Два элемента - рост
    assert get_pct_growth([100, 120]) == [None, 20]
    # Два элемента - падение
    assert get_pct_growth([100, 80]) == [None, -20]
    # Отрицательные значения
    assert get_pct_growth([-100, -50]) == [None, -50]
    # Дробные значения
    result = get_pct_growth([10, 15, 7.5])
    expected = [None, 50, -50]
    assert result == expected

