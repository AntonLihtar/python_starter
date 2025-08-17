"""
Напишите функцию, которая возвращает true, если число является четным.
Подсказка: используйте % для определения остатка от деления: 10 % 3 = 1
"""

def is_odd(n: int) -> bool:
    return n % 2 == 0

if __name__ == "__main__":

    test_numbers = [10, 0, 7, 6, 14, -57]
    for num in test_numbers:
        print(f"{num}: {is_odd(num)}")