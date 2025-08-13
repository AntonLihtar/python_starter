import pytest
from tasks3.task1 import two_lists_to_dict
from tasks3.task2 import concat_dicts
from tasks3.task3 import sort_dict_values
from tasks3.task4 import to_yearly_sales


def test_two_lists_to_dict():
    keys = ["USA", "Russia", "France"]
    values = [100, 10, 25]
    assert two_lists_to_dict(keys, values) == {"USA": 100, "Russia": 10, "France": 25}

    # Тест 2: пустые списки
    assert two_lists_to_dict([], []) == {}

    # Тест 3: списки с одним элементом
    assert two_lists_to_dict(["key"], [42]) == {"key": 42}

    # Тест 4: списки с разными типами данных
    keys = [1, "two", 3.0]
    values = [True, None, "three"]
    assert two_lists_to_dict(keys, values) == {1: True, "two": None, 3.0: "three"}

    # Тест 5: второй список длиннее — лишние элементы игнорируются
    keys = ["a", "b"]
    values = [1, 2, 3, 4]
    assert two_lists_to_dict(keys, values) == {"a": 1, "b": 2}

    # Тест 6: первый список длиннее — лишние элементы игнорируются
    keys = ["a", "b", "c", "d"]
    values = [1, 2]
    assert two_lists_to_dict(keys, values) == {"a": 1, "b": 2}

    # Тест 7: списки с дубликатами в ключах — последнее значение побеждает
    keys = ["a", "b", "a"]
    values = [1, 2, 3]
    assert two_lists_to_dict(keys, values) == {"a": 3, "b": 2}

def test_move_zeros():  # Тест 1: обычные словари
    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3, 'd': 4}
    assert concat_dicts(d1, d2) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # Тест 2: пустые словари
    assert concat_dicts({}, {}) == {}
    assert concat_dicts({'a': 1}, {}) == {'a': 1}
    assert concat_dicts({}, {'b': 2}) == {'b': 2}

    # Тест 3: пересекающиеся ключи — второй словарь побеждает
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 20, 'c': 3}
    assert concat_dicts(d1, d2) == {'a': 1, 'b': 20, 'c': 3}

    # Тест 4: один и тот же словарь
    d = {'x': 1}
    assert concat_dicts(d, d) == {'x': 1}

    # Тест 5: разные типы значений
    d1 = {'name': 'Alice', 'age': 30}
    d2 = {'city': 'NYC', 'age': 31}
    assert concat_dicts(d1, d2) == {'name': 'Alice', 'age': 31, 'city': 'NYC'}


    # Тест 6: большие словари
    d1 = {f'key{i}': i for i in range(100)}
    d2 = {f'key{i}': i * 2 for i in range(50, 150)}
    result = concat_dicts(d1, d2)
    assert len(result) == 150
    assert result['key0'] == 0
    assert result['key100'] == 200

    # Тест 7: None в значениях
    d1 = {'a': None, 'b': 1}
    d2 = {'a': 2, 'c': None}
    assert concat_dicts(d1, d2) == {'a': 2, 'b': 1, 'c': None}

def test_sort_dict_values():
    # Тест 1: обычный словарь
    d = {
        "USA": 100,
        "Japan": 90,
        "France": 25,
        "China": 80,
        "India": 50,
        "Russia": 5
    }
    expected = {
        "USA": 100,
        "Japan": 90,
        "China": 80,
        "India": 50,
        "France": 25,
        "Russia": 5
    }
    assert sort_dict_values(d) == expected

    # Тест 2: пустой словарь
    assert sort_dict_values({}) == {}

    # Тест 3: один элемент
    assert sort_dict_values({"A": 42}) == {"A": 42}

    # Тест 4: уже отсортированный словарь
    d = {"A": 100, "B": 50, "C": 10}
    assert sort_dict_values(d) == {"A": 100, "B": 50, "C": 10}
    # Тест 5: отрицательные значения
    d = {"A": -10, "B": 5, "C": -20}
    assert sort_dict_values(d) == {"B": 5, "A": -10, "C": -20}

    # Тест 6: одинаковые значения
    d = {"A": 50, "B": 50, "C": 30}
    assert sort_dict_values(d) == {"A": 50, "B": 50, "C": 30}

    # Тест 7: строки как значения
    d = {"A": "zebra", "B": "apple", "C": "banana"}
    assert sort_dict_values(d) == {"A": "zebra", "C": "banana", "B": "apple"}

    # Тест 8: float значения
    d = {"A": 3.14, "B": 2.71, "C": 1.41}
    assert sort_dict_values(d) == {"A": 3.14, "B": 2.71, "C": 1.41}

    # Тест 9: большие числа
    d = {"A": 1000000, "B": 1, "C": 999999}
    assert sort_dict_values(d) == {"A": 1000000, "C": 999999, "B": 1}

    # Тест 10: проверка, что исходный словарь не изменился
    original = {"x": 10, "y": 5, "z": 15}
    original_copy = original.copy()
    result = sort_dict_values(original)
    assert original == original_copy  # исходный не изменился
    assert result == {"z": 15, "x": 10, "y": 5}

def test_to_yearly_sales():
    # Тест 1: обычные данные
    monthly_sales = {
        "Jan_2020": 100,
        "Feb_2020": 90,
        "Mar_2020": 15,
        "Jan_2021": 10,
        "Feb_2021": 50,
        "Mar_2022": 5,
        "Sep_2023": 12,
        "Oct_2023": 12
    }
    expected = {
        "2020": 205,  # 100 + 90 + 15
        "2021": 60,   # 10 + 50
        "2022": 5,    # 5
        "2023": 24    # 12 + 12
    }
    assert to_yearly_sales(monthly_sales) == expected

    # Тест 2: пустой словарь
    assert to_yearly_sales({}) == {}

    # Тест 3: один месяц
    assert to_yearly_sales({"Jan_2020": 100}) == {"2020": 100}

    # Тест 4: несколько месяцев одного года
    sales = {
        "Jan_2020": 10,
        "Feb_2020": 20,
        "Mar_2020": 30,
        "Apr_2020": 40
    }
    assert to_yearly_sales(sales) == {"2020": 100}

    # Тест 5: одинаковые месяцы разных лет
    sales = {
        "Jan_2020": 100,
        "Jan_2021": 200,
        "Jan_2022": 300
    }
    expected = {"2020": 100, "2021": 200, "2022": 300}
    assert to_yearly_sales(sales) == expected

    # Тест 6: нулевые значения
    sales = {
        "Jan_2020": 0,
        "Feb_2020": 50,
        "Mar_2020": 0
    }
    assert to_yearly_sales(sales) == {"2020": 50}

    # Тест 7: отрицательные значения
    sales = {
        "Jan_2020": 100,
        "Feb_2020": -20,
        "Mar_2020": 30
    }
    assert to_yearly_sales(sales) == {"2020": 110}

    # Тест 8: возвращаемый тип — обычный dict
    result = to_yearly_sales({"Jan_2020": 100})
    assert isinstance(result, dict)
    assert not hasattr(result, 'default_factory')  # не defaultdict

    # Тест 9: много лет
    sales = {
        "Jan_2020": 10,
        "Jan_2021": 20,
        "Jan_2022": 30,
        "Jan_2023": 40,
        "Jan_2024": 50
    }
    expected = {"2020": 10, "2021": 20, "2022": 30, "2023": 40, "2024": 50}
    assert to_yearly_sales(sales) == expected

    # Тест 10: большие числа
    sales = {
        "Jan_2020": 1000000,
        "Feb_2020": 500000,
        "Jan_2021": 2000000
    }
    assert to_yearly_sales(sales) == {"2020": 1500000, "2021": 2000000}




