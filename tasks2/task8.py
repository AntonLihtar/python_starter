"""
    Напишите функцию, которая вернет true, если список является полностью возрастающим,
    т.е. каждый следующий элемент больше предыдущего
"""


def is_list_growing(lst: list[float]) -> bool:
    if len(lst) < 2:
        return True
    a = lst[0]
    for number in lst[1:]:
        if not a < number:
            return False
        a = number
    return True


if __name__ == "__main__":

    test_nums = [[1, 2, 3], [4, 3, 5], [10.2, 10.3, 10.4], [-5, -3, 0]]
    for num in test_nums:
        print(f"{num}: {is_list_growing(num)}")
