"""
    Показать сумму покупок по категориями. Отсортировать категории по возрастанию суммы
"""
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


def get_sorted_category_sum(d):
    obj = {}
    for el in d:
        category = el['category']
        obj.setdefault(category, 0)
        obj[category] += el['price_rub'] * el['count']
    return sorted(obj.items(), key=lambda x: x[1])

if __name__ == "__main__":
    res = get_sorted_category_sum(_sales_data)
    print(res)

    # [("bakery", 115),
    #  ("drinks", 390),
    #  ("dairy products", 440),
    #  ]
