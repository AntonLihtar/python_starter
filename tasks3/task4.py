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

def to_yearly_sales(d: dict):
    ob = {}
    for k, v in d.items():
        key = k.split('_')[1]
        ob.setdefault(key, 0)
        ob[key] += v
    return ob


if __name__ == "__main__":
    print(to_yearly_sales(monthly_sales))
    #  {
    #     "2020": 205,
    #     "2021": 60,
    #     "2022": 5,
    #     "2023": 24
    # }
