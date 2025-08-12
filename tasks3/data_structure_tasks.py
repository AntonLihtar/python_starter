from task1 import two_lists_to_dict
# from dictionary_tasks import fill_missed_years, get_sorted_category_sum, \
#     get_distinct_categories, \
#     concat_dicts, sort_dict_values, to_yearly_sales


def test_to_lists_to_dict():
    """
        Соединить два списка в словарь
    """
    keys = ["USA", "Russia", "France"]
    income = [100, 10, 25]
    assert two_lists_to_dict(keys, income) == {
        "USA": 100,
        "Russia": 10,
        "France": 25
    }


def test_merge_two_dicts():
    """
        Соединить два словаря
    """
    developed_markets = {
        "USA": 100,
        "Japan": 90,
        "France": 25
    }

    emerging_markets = {
        "China": 80,
        "India": 50,
        "Russia": 5
    }

    assert concat_dicts(developed_markets, emerging_markets) == {
        "USA": 100,
        "Japan": 90,
        "France": 25,
        "China": 80,
        "India": 50,
        "Russia": 5
    }


def test_sort_dict_values():
    """
        Отсортировать словарь по убыванию
    """
    d = {
        "USA": 100,
        "Japan": 90,
        "France": 25,
        "China": 80,
        "India": 50,
        "Russia": 5
    }
    assert sort_dict_values(d) == {
        "USA": 100,
        "Japan": 90,
        "China": 80,
        "India": 50,
        "France": 25,
        "Russia": 5
    }


def test_sum_value_of_the_same_key_kinds():
    """
        Просуммировать словарь по годам
    """
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
    assert to_yearly_sales(monthly_sales) == {
        "2020": 205,
        "2021": 60,
        "2022": 5,
        "2023": 24
    }


def test_fill_missed_years():
    """
        Заполнить пропущенные значения средним арифметическим двух соседних значений.
        Например, если в 2015 году значение равно 50, в 2018 - 80, 
        то в 2016 должно быть 60, в 2017 - 70
    """
    yearly_sales = {
        "2015": 50,
        "2018": 65,
        "2019": 120,
        "2023": 160,
        "2025": 200
    }

    assert fill_missed_years(yearly_sales) == {
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


_sales_data = [
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


def test_get_distinct_categories():
    """
        Вернуть множество уникальных категорий товаров
        Воспользоваться set comprehension (по аналогии с list/dict comprehension)
    """

    assert get_distinct_categories(_sales_data) == {
        "dairy products", "bakery", "drinks"}


def test_sum_category_as_tuples():
    """
        Показать сумму покупок по категориями. Отсортировать категории по возрастанию суммы
    """
    actual = get_sorted_category_sum(_sales_data)
    assert actual == [("bakery", 115),
                      ("drinks", 390),
                      ("dairy products", 440),
                      ]
