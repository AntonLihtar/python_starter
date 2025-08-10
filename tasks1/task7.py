"""
    Дана ФИО, напишите функцию, которая выводит фамилию и инициалы через точку.
    Например: "Лермонтов Михаил Юрьевич" -> "Лермонтов М. Ю."
"""


def get_person_short_name(fio: str) -> str:
    f, i, o = fio.title().split()
    return f'{f} {i[0]}. {o[0]}.'

if __name__ == "__main__":

    test_strings = [
        'аsss роза упала',
        'Александр Сергеевич Пушкин',
        'литс или стил'
    ]
    for num in test_strings:
        print(f"{num}: {get_person_short_name(num)}")
