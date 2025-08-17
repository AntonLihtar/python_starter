"""
    Напишите функцию, которая принимает три положительных числа и
    возвращает вид треугольника (равносторонний, равнобедренный, обычный).
"""


def get_triangle_kind(a: int, b: int, c: int) -> str:
    if a <= 0 or b <= 0 or c <= 0 or a + b + c != 180:
        return "некорректные значения"
    if a == b and b == c:
        return "равносторонний"
    if a == b or a == c or b == c:
        return "равнобедренный"
    return "обычный"


if __name__ == "__main__":

    test_numbers = [[60, 50, 70], [30, 75, 75], [60, 60, 60], [120, 30, 30], [-16, 0, 120]]
    for num in test_numbers:
        print(f"{num}: {get_triangle_kind(num[0], num[1], num[2])}")
