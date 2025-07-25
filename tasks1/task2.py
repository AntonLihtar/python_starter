"""
Напишите функцию, которая возращает true, если число является простым
"""

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


if __name__ == "__main__":

    test_numbers = [10, 0, 7, -2, 1, 3, 15, 14]
    for num in test_numbers:
        print(f"{num}: {is_prime(num)}")
