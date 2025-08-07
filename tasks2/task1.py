"""
    Нужно реализовать надпись в формате "N просмотров". Падеж слова "просмотр" зависит
    от числа N. Например, 1 просмотр, 2 просмотра и т.п.
"""

def get_views_count(n: int) -> str:
    txt = ""
    if 1 < n < 5: txt = "а"
    if 4 < n or n == 0: txt = "ов"
    if n < 0: raise ValueError("n не может быть отрицательным")
    return f'{n} просмотр{txt}'


if __name__ == "__main__":
    numbers = [10, 0, 2, 1, 7, 6, 14, -57]
    try:
        for x in numbers:
            print(get_views_count(x))
    except ValueError as err:
        print(err)
    finally:
        print('end')
