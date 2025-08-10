"""
    Дан список целых чисел и определенное заданное число. Найти все пары из списка,
    сумма которых равна этому числу.
    Верните из функции список кортежей.
    Например: get_pairs_number([1, 2, 4, 3, 5, 2], 7) -> [(4,3), (5,2)]
"""


def get_pairs_number(lst: list[int], n) -> list[tuple]:
    pairs = set()
    for i, v in enumerate(lst):
        for v2 in lst[i + 1:]:
            if v + v2 == n:
                value = tuple(sorted((v, v2), reverse=True))
                pairs.add(value)

    return list(pairs)


if __name__ == "__main__":
    print(get_pairs_number([1, 2, 4, 3, 5, 2], 7))
