"""
    Соединить два словаря
"""

# не меняем текущие словари
def concat_dicts(sl1, sl2):
    ns = sl1.copy()
    ns.update(sl2)
    return ns

if __name__ == "__main__":
    developed_markets = {
        "USA": 100,
        "Japan": 90,
        "France": 25
    }

    emerging_markets = {
        "China": 80,
        "India": 50,
        "Russia": 5
    }
    print(concat_dicts(developed_markets, emerging_markets))
