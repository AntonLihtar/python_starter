"""
    Соединить два списка в словарь
"""


def two_lists_to_dict(lst1: list, lst2: list) -> dict:
    return dict(zip(lst1, lst2))


if __name__ == "__main__":
    keys = ["USA", "Russia", "France"]
    income = [100, 10, 25]
    print(two_lists_to_dict(keys, income))
