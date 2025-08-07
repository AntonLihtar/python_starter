"""
    Дан список, содержащий нули. Вернуть список, где все нули сдвинуты вправо,
    сохранив порядок исходного списка:
    move_zeros([1, 0, 0, 2, 3, 0, 1]) -> [1, 2, 3, 1, 0, 0, 0]

    Решить в двух вариантах:
    - функция принимаем список и возвращает НОВЫЙ список
    - функция изменяет список, который был передан в аргументе функции
    (функция ничего не возвращает)
"""


def move_zeros(lst: list[float]) -> list:
    new_arr = [x for x in lst if x != 0]
    zeros_arr = [0]  * lst.count(0)
    return [*new_arr, *zeros_arr]

def move_zeros2(lst: list[float]):
    new_arr = [x for x in lst if x != 0]
    zeros_arr = [0]  * lst.count(0)
    lst.clear()
    lst.extend(new_arr + zeros_arr)

def move_zeros_v2(lst: list[float]) -> list:
    new_arr = []
    new_z = []
    for el in lst:
        if el == 0:
            new_z.append(0)
        else:
            new_arr.append(el)
    return new_arr + new_z

if __name__ == "__main__":
    print(move_zeros([1, 0, 0, 2, 3, 0, 1]))

    arr = [1, 0, 0, 2, 3, 0, 1]
    move_zeros2(arr)
    print(arr)

    print(move_zeros_v2([1, 0, 0, 2, 3, 0, 1]))
