"""
    Дан массив цен акций, вывести список, содержащий темпы прироста от периода к периоду.
    Для первого элемента списка выведите значение None. Округлите до целых.
    Например: [100, 150, 300, 400] -> [None, 50%, 100%, 33%]
"""


def get_pct_growth(s: list[float]) -> list[float]:
    arr = []
    for i, v in enumerate(s):
        if i == 0:
            arr.append(None)
            continue
        arr.append(round(v / s[i - 1] * 100) - 100)
    return arr


def get_pct_growth2(s: list[float]) -> list[float | None]:
    arr: list[float | None] = []
    if len(s) > 0: arr.append(None)
    for i in range(1, len(s)):
        growth = s[i] / s[i - 1] * 100 - 100
        arr.append(round(growth))
    return arr


if __name__ == "__main__":
    print(get_pct_growth([100, 150, 300, 400]))
    print(get_pct_growth2([100, 150, 300, 400]))
