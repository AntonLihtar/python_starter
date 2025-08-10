"""
    Дан массив цен акций, вывести список, содержащий темпы прироста от периода к периоду.
    Для первого элемента списка выведите значение None. Округлите до целых.
    Например: [100, 150, 300, 400] -> [None, 50%, 100%, 33%]
"""

#  вот так лучше!
#  а где обработка ошибок?
# list comprehension,
# zip, slice
# def f(x,lst):
#   pass

# [f(x) for x in lst]
s = [10, 20, 0, 30, 40]  # если 0 вернуть None
s1 = [10, None, 30, None]  # если None вернуть None


def get_pct_growth(s: list[float]) -> list[float | None]:
    if len(s) == 0:
        return []

    def get_r(prev: float | None, curr: float | None) -> float | None:
        if prev in (0, None) or curr in (0, None):
            return None
        x = curr / prev * 100 - 100
        return round(x)

    arr = [get_r(*el) for el in zip(s, s[1:])]
    return [None] + arr


if __name__ == "__main__":
    print(get_pct_growth([100, 150, 300, 400]))
    print(get_pct_growth(s))
    print(get_pct_growth(s1))
    print(get_pct_growth([100, None, 200, 50, 150, 0, 200]))
