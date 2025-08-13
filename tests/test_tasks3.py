import pytest
from tasks3.task1 import two_lists_to_dict
from tasks3.task2 import concat_dicts
from tasks3.task3 import sort_dict_values
from tasks3.task4 import to_yearly_sales
from tasks3.task5 import fill_missed_years
from tasks3.task6 import get_distinct_categories
from tasks3.task7 import get_sorted_category_sum


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

def test_fill_missed_years():
    # Тест 1: основной пример из условия
    yearly_sales = {
        "2015": 50,
        "2018": 65,
        "2019": 120,
        "2023": 160,
        "2025": 200
    }
    expected = {
        "2015": 50,
        "2016": 55,
        "2017": 60,
        "2018": 65,
        "2019": 120,
        "2020": 130,
        "2021": 140,
        "2022": 150,
        "2023": 160,
        "2024": 180,
        "2025": 200
    }
    assert fill_missed_years(yearly_sales) == expected

    # Тест 2: пустой словарь
    assert fill_missed_years({}) == {}

    # Тест 3: один год
    assert fill_missed_years({"2020": 100}) == {"2020": 100}

    # Тест 4: два года подряд (нет пропусков)
    sales = {"2020": 100, "2021": 150}
    expected = {"2020": 100, "2021": 150}
    assert fill_missed_years(sales) == expected

    # Тест 5: два года с пропуском
    sales = {"2020": 100, "2023": 160}
    expected = {"2020": 100, "2021": 120, "2022": 140, "2023": 160}
    assert fill_missed_years(sales) == expected

    # Тест 6: один пропущенный год
    sales = {"2020": 100, "2022": 140}
    expected = {"2020": 100, "2021": 120, "2022": 140}
    assert fill_missed_years(sales) == expected

    # Тест 7: отрицательные значения
    sales = {"2020": -10, "2023": 20}
    expected = {"2020": -10, "2021": 0, "2022": 10, "2023": 20}
    assert fill_missed_years(sales) == expected

    # Тест 8: нулевые значения
    sales = {"2020": 0, "2022": 10}
    expected = {"2020": 0, "2021": 5, "2022": 10}
    assert fill_missed_years(sales) == expected

    # Тест 9: неотсортированные ключи
    sales = {"2023": 160, "2015": 50, "2025": 200, "2018": 65, "2019": 120}
    expected = {
        "2015": 50,
        "2016": 55,
        "2017": 60,
        "2018": 65,
        "2019": 120,
        "2020": 130,
        "2021": 140,
        "2022": 150,
        "2023": 160,
        "2024": 180,
        "2025": 200
    }
    assert fill_missed_years(sales) == expected

    # Тест 10: большие числа
    sales = {"2020": 1000, "2024": 1800}
    expected = {
        "2020": 1000,
        "2021": 1200,
        "2022": 1400,
        "2023": 1600,
        "2024": 1800
    }
    assert fill_missed_years(sales) == expected

    # Тест 11: убывающие значения
    sales = {"2020": 100, "2023": 40}
    expected = {"2020": 100, "2021": 80, "2022": 60, "2023": 40}
    assert fill_missed_years(sales) == expected

    # Тест 12: проверка, что исходный словарь не изменяется
    original = {"2020": 100, "2023": 160}
    original_copy = original.copy()
    result = fill_missed_years(original)
    assert original == original_copy  # исходный не изменился
    assert result == {"2020": 100, "2021": 120, "2022": 140, "2023": 160}

def test_get_distinct_categories():
    # Test 1: basic functionality
    sales_data = [
        {
            "category": "dairy products",
            "product": "milk",
            "price_rub": 100,
            "count": 1
        },
        {
            "category": "dairy products",
            "product": "cream",
            "price_rub": 290,
            "count": 1
        },
        {
            "category": "bakery",
            "product": "white_bread",
            "price_rub": 60,
            "count": 1
        },
        {
            "category": "drinks",
            "product": "water",
            "price_rub": 90,
            "count": 1
        }
    ]
    expected = {"dairy products", "bakery", "drinks"}
    assert get_distinct_categories(sales_data) == expected

    # Test 2: empty list
    assert get_distinct_categories([]) == set()

    # Test 3: single item
    single_item = [{"category": "electronics", "product": "phone", "price_rub": 500, "count": 1}]
    assert get_distinct_categories(single_item) == {"electronics"}

    # Test 4: all items same category
    same_category = [
        {"category": "books", "product": "novel", "price_rub": 600, "count": 1},
        {"category": "books", "product": "magazine", "price_rub": 200, "count": 1},
        {"category": "books", "product": "textbook", "price_rub": 800, "count": 1}
    ]
    assert get_distinct_categories(same_category) == {"books"}

    # Test 5: many duplicate categories
    many_duplicates = [
        {"category": "food", "product": "apple", "price_rub": 50, "count": 1},
        {"category": "food", "product": "banana", "price_rub": 30, "count": 1},
        {"category": "food", "product": "orange", "price_rub": 40, "count": 1},
        {"category": "clothes", "product": "shirt", "price_rub": 1000, "count": 1},
        {"category": "clothes", "product": "pants", "price_rub": 1500, "count": 1},
        {"category": "food", "product": "grape", "price_rub": 60, "count": 1}
    ]
    assert get_distinct_categories(many_duplicates) == {"food", "clothes"}

    # Test 6: categories with special characters
    special_chars = [
        {"category": "food & drinks", "product": "soda", "price_rub": 100, "count": 1},
        {"category": "home & garden", "product": "plant", "price_rub": 300, "count": 1},
        {"category": "food & drinks", "product": "juice", "price_rub": 150, "count": 1}
    ]
    expected = {"food & drinks", "home & garden"}
    assert get_distinct_categories(special_chars) == expected

    # Test 7: empty category names
    empty_categories = [
        {"category": "", "product": "item1", "price_rub": 100, "count": 1},
        {"category": "normal", "product": "item2", "price_rub": 200, "count": 1},
        {"category": "", "product": "item3", "price_rub": 300, "count": 1}
    ]
    assert get_distinct_categories(empty_categories) == {"", "normal"}

    # Test 8: numeric category names (as strings)
    numeric_categories = [
        {"category": "123", "product": "item1", "price_rub": 100, "count": 1},
        {"category": "456", "product": "item2", "price_rub": 200, "count": 1},
        {"category": "123", "product": "item3", "price_rub": 300, "count": 1}
    ]
    assert get_distinct_categories(numeric_categories) == {"123", "456"}

    # Test 9: very long category names
    long_names = [
        {"category": "a" * 100, "product": "item1", "price_rub": 100, "count": 1},
        {"category": "b" * 100, "product": "item2", "price_rub": 200, "count": 1},
        {"category": "a" * 100, "product": "item3", "price_rub": 300, "count": 1}
    ]
    assert get_distinct_categories(long_names) == {"a" * 100, "b" * 100}

    # Test 11: original data unchanged
    original_data = [
        {"category": "test", "product": "item1", "price_rub": 100, "count": 1},
        {"category": "test", "product": "item2", "price_rub": 200, "count": 1}
    ]
    original_copy = [item.copy() for item in original_data]
    result = get_distinct_categories(original_data)
    assert result == {"test"}
    # Check that original data structure is unchanged
    assert len(original_data) == len(original_copy)
    for i, item in enumerate(original_data):
        assert item == original_copy[i]

def test_get_sorted_category_sum():
    # Тест 1: основной пример из условия
    sales_data = [
        {
            "category": "dairy products",
            "product": "milk",
            "price_rub": 100,
            "count": 1
        },
        {
            "category": "dairy products",
            "product": "cream",
            "price_rub": 290,
            "count": 1
        },
        {
            "category": "dairy products",
            "product": "yogurt",
            "price_rub": 50,
            "count": 1
        },
        {
            "category": "bakery",
            "product": "white_bread",
            "price_rub": 60,
            "count": 1
        },
        {
            "category": "bakery",
            "product": "black_bread",
            "price_rub": 55,
            "count": 1
        },
        {
            "category": "drinks",
            "product": "water",
            "price_rub": 90,
            "count": 1
        },
        {
            "category": "drinks",
            "product": "apple_juice",
            "price_rub": 300,
            "count": 1
        }
    ]
    expected = [("bakery", 115), ("drinks", 390), ("dairy products", 440)]
    assert get_sorted_category_sum(sales_data) == expected

    # Тест 2: пустой список
    assert get_sorted_category_sum([]) == []

    # Тест 3: одна категория, один товар
    single_item = [{"category": "electronics", "product": "phone", "price_rub": 1000, "count": 1}]
    assert get_sorted_category_sum(single_item) == [("electronics", 1000)]

    # Тест 4: одна категория, несколько товаров
    multiple_items = [
        {"category": "books", "product": "novel", "price_rub": 300, "count": 1},
        {"category": "books", "product": "magazine", "price_rub": 100, "count": 1},
        {"category": "books", "product": "textbook", "price_rub": 400, "count": 1}
    ]
    assert get_sorted_category_sum(multiple_items) == [("books", 800)]

    # Тест 5: несколько категорий с одинаковой суммой
    equal_sums = [
        {"category": "A", "product": "item1", "price_rub": 100, "count": 1},
        {"category": "B", "product": "item2", "price_rub": 50, "count": 1},
        {"category": "B", "product": "item3", "price_rub": 50, "count": 1},
        {"category": "C", "product": "item4", "price_rub": 100, "count": 1}
    ]
    # Сортировка стабильна, но по значению - A и C равны, B = 100
    result = get_sorted_category_sum(equal_sums)
    assert len(result) == 3
    assert ("A", 100) in result
    assert ("B", 100) in result
    assert ("C", 100) in result

    # Тест 6: нулевые цены
    zero_prices = [
        {"category": "free", "product": "sample", "price_rub": 0, "count": 1},
        {"category": "paid", "product": "item", "price_rub": 100, "count": 1}
    ]
    assert get_sorted_category_sum(zero_prices) == [("free", 0), ("paid", 100)]

    # Тест 7: отрицательные цены (допустимо для скидок)
    negative_prices = [
        {"category": "discounted", "product": "item1", "price_rub": -50, "count": 1},
        {"category": "regular", "product": "item2", "price_rub": 100, "count": 1}
    ]
    assert get_sorted_category_sum(negative_prices) == [("discounted", -50), ("regular", 100)]

    # Тест 8: большие числа
    big_numbers = [
        {"category": "luxury", "product": "watch", "price_rub": 100000, "count": 1},
        {"category": "budget", "product": "pen", "price_rub": 10, "count": 1}
    ]
    assert get_sorted_category_sum(big_numbers) == [("budget", 10), ("luxury", 100000)]

    # Тест 9: категории с одинаковыми именами, но разными товарами
    duplicate_categories = [
        {"category": "food", "product": "apple", "price_rub": 50, "count": 2},  # 100
        {"category": "food", "product": "banana", "price_rub": 30, "count": 3}, # 90
        {"category": "clothes", "product": "shirt", "price_rub": 500, "count": 1} # 500
    ]
    assert get_sorted_category_sum(duplicate_categories) == [("food", 190), ("clothes", 500)]

    # Тест 10: специальные символы в названиях категорий
    special_chars = [
        {"category": "food & drinks", "product": "soda", "price_rub": 100, "count": 1},
        {"category": "home & garden", "product": "plant", "price_rub": 300, "count": 1},
        {"category": "food & drinks", "product": "juice", "price_rub": 150, "count": 1}
    ]
    expected = [("food & drinks", 250), ("home & garden", 300)]
    assert get_sorted_category_sum(special_chars) == expected

    # Тест 11: проверка типа возвращаемого значения
    result = get_sorted_category_sum([{"category": "test", "product": "item", "price_rub": 100, "count": 1}])
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], tuple)
    assert len(result[0]) == 2

    # Тест 12: товары с количеством > 1 (если нужно учитывать count)
    with_count = [
        {"category": "bulk", "product": "apples", "price_rub": 50, "count": 3},  # 150
        {"category": "single", "product": "orange", "price_rub": 30, "count": 1} # 30
    ]
    result = get_sorted_category_sum(with_count)
    assert result == [("single", 30), ("bulk", 150)]



