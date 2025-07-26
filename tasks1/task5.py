"""
    Проверить, является ли строка с пробелами палиндромом (а роза упала на лапу азора).
    Упростим задачу, допуская, что cлова в предложении разделяются только одним пробелом.
"""


def is_palindrom(s: str) -> bool:
    # через массив
    arr = []
    for char in s:
        if char != ' ':
            arr.append(char.lower())

    len_arr = len(arr)
    max_length = int(len_arr / 2)

    for char in range(max_length):
        a = arr[char]
        b = arr[len_arr - (char + 1)]
        if a != b:
            return False
    return True

def is_palindrom2(s: str) -> bool:
    # через строки
    str1 = ''.join(s.split()).lower()
    return str1 == str1[::-1]


if __name__ == "__main__":

    test_numbers = [
        'а роза упала на лапу азора',
        'тест стис',
        'литс или стил'
    ]
    for num in test_numbers:
        print(f"{num}: {is_palindrom(num)}")
        print(f"{num}: {is_palindrom2(num)}")

