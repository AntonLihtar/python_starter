"""
    Нужно реализовать надпись в формате "N просмотров". Падеж слова "просмотр" зависит
    от числа N. Например, 1 просмотр, 2 просмотра и т.п.
"""


def get_views_count(n: int) -> str:
    if n < 0:
        raise ValueError("n не может быть отрицательным")

    # Проверяем последние две цифры
    if 11 <= n % 100 <= 14:
        return f"{n} просмотров"

    # Проверяем последнюю цифру
    last_digit = n % 10
    if last_digit == 1:
        return f"{n} просмотр"
    elif last_digit in (2, 3, 4):
        return f"{n} просмотра"
    else:
        return f"{n} просмотров"


if __name__ == "__main__":
    numbers = [152, 144, 763, 102, 204,12, 212]
    numbers2 = [10, 0, 2, 1, 7, 6, 14, -57, 11, 51, 111, 121, 191]
    try:
        for x in numbers2:
            print(get_views_count(x))
    except ValueError as err:
        print(err)
    finally:
        print('end')
