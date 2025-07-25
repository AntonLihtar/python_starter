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

    lenArr = len(arr)
    maxLenght = int(lenArr / 2)

    for char in range(maxLenght):
        a = arr[char]
        b = arr[lenArr - (char + 1)]
        if a != b:
            return False
    return True

def is_palindrom2(s: str) -> bool:
    # через строки
    str = ''.join(s.split()).lower()
    return str == str[::-1]


if __name__ == "__main__":

    test_numbers = [
        'а роза упала на лапу азора',
        'тест стис',
        'литс или стил'
    ]
    for num in test_numbers:
        print(f"{num}: {is_palindrom(num)}")
        print(f"{num}: {is_palindrom2(num)}")

