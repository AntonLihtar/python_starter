from collections import Counter

def get_most_frequent_symbol(s: str) -> tuple[str, int]:
    """
        Вернуть символ (и число символов), который встречается в строке чаще всего независимо
        от порядка. Например:
        get_most_frequent_symbol("aaeeaeabenbdedeeeddaaadffeffseee") == (e, 12)
        Темы: парсинг строк, словарь
    """
    if not s:
        return '', 0

    counters = Counter(s)
    return counters.most_common(1)[0]



if __name__ == "__main__":
    print(get_most_frequent_symbol('aaeeaeabenbdedeeeddaaadffeffseee'))
