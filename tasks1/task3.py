"""
Напишите функцию, которая возвращает true, если
три заданных числа (в указанном порядке) являются последовательными членами
арифметической прогрессии
"""


def is_arifm_progression(a: int, b: int, c: int) -> bool:
    return (b-a) == (c-b)

if __name__ == "__main__":

    test_numbers = [[-9,  -7 , -5], [4, 8, 12], [7, 8, 11], [0, 1, 2]]
    for num in test_numbers:
        print(f"{num}: {is_arifm_progression(num[0], num[1], num[2])}")
