"""
Напишите функцию, которая возвращает true, если число является четным.
Подсказка: используйте % для определения остатка от деления: 10 % 3 = 1
"""

def is_odd(n: int) -> bool:
    return n % 2 == 0

def is_odd2(n: int) -> bool:
    return True if n % 2 == 0 else False

def is_odd3(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd4(n: int) -> bool:
    x = False
    if n % 2 == 0:
        x = True
    return x

if __name__ == "__main__":

    test_numbers = [10, 0, 7, 6, 14, -57]
    for num in test_numbers:
        print(f"{num}: {is_odd(num)}")