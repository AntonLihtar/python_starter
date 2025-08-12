"""
    Отсортировать словарь по убыванию
"""
d = {
    "USA": 100,
    "Japan": 90,
    "France": 25,
    "China": 80,
    "India": 50,
    "Russia": 5
}

def sort_dict_values(dct: dict) -> dict:
    ls = dict(sorted(dct.items(), key=lambda x: x[1], reverse=True))
    return ls

if __name__ == "__main__":
    print(sort_dict_values(d))
