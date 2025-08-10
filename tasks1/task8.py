"""
    Напишите функцию, которая вернет true, если список является полностью возрастающим,
    т.е. каждый следующий элемент больше предыдущего
"""


def is_list_growing(lst: list[float]) -> bool:
    if len(lst) < 2:
        return True
    res = [lst[x] < lst[x + 1] for x in range(len(lst) - 1)]  # 2v
    return all(res)


if __name__ == "__main__":

    test_nums = [[1, 2, 3], [4, 3, 5], [10.2, 10.3, 10.4], [-5, -3, 0]]
    for num in test_nums:
        print(f"{num}: {is_list_growing(num)}")
