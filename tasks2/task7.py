"""
    Дана ФИО, напишите функцию, которая выводит фамилию и инициалы через точку.
    Например: "Лермонтов Михаил Юрьевич" -> "Лермонтов М. Ю."
"""


def get_person_short_name(fio: str) -> str:
    if fio == '':
        return fio
    arr = fio.title().split()
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return f'{arr[0]} {arr[1][0]}.'
    return f'{arr[0]} {arr[1][0]}. {arr[2][:1]}.'


def get_person_short_name2(fio: str) -> str:
    new_str = ''
    arr = fio.title().split()
    for index in range(len(arr)):
        if index == 3:
            break
        if index != 0:
            new_str += f' {arr[index][0]}.'
        else:
            new_str += f'{arr[index]}'
    return new_str


if __name__ == "__main__":

    test_strings = [
        'аsss роза упала на лапу азора',
        'Александр Сергеевич Пушкин',
        'литс или стил'
    ]
    for num in test_strings:
        print(f"{num}: {get_person_short_name(num)}")
