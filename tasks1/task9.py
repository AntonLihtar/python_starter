"""
    Дан список целых чисел и определенное заданное число. Найти все пары из списка,
    сумма которых равна этому числу.
    Верните из функции список кортежей.
    Например: get_pairs_number([1, 2, 4, 3, 5, 2], 7) -> [(4,3), (5,2)]
"""


def get_pairs_number(lst: list[int], n) -> list[tuple]:
    """
    первый вариант по тз - сравниваем все ПАРЫ между собой
    """
    pairs = []
    if len(lst) < 1:
        return pairs
    if len(lst) == 1 and lst[0] == n:
        return [(n,)]

    a = lst[0]
    for b in lst[1:]:
        if a + b == n:
            pairs.append((a, b))
        a = b
    return pairs


def get_pairs_number2(lst: list[int], n) -> list[tuple]:
    """
    второй вариант - сравниваем все ЧИСЛА массива между собой
    """
    pairs = []
    if len(lst) < 1:
        return pairs
    if len(lst) == 1 and lst[0] == n:
        return [(n,)]

    for index, A in enumerate(lst):
        for B in lst[index + 1:]:
            if A + B == n:
                pairs.append((A, B))

    # Удаляем дубликаты
    unique_pairs = []
    for pair in pairs:
        # получаем отсортированый кортеж дял сравнения
        new_pair = tuple(sorted(pair))
        if new_pair not in unique_pairs:
            unique_pairs.append(new_pair)
    return unique_pairs


if __name__ == "__main__":
    print(get_pairs_number([1, 2, 4, 3, 5, 2], 7))
    print(get_pairs_number2([1, 2, 4, 3, 5, 2], 7))
