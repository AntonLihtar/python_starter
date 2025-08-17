"""
    Данные загрузились из БД с лишними символами, а должны быть только русские буквы.
    Напишите функцию, которая удаляет символы, которые не являются русскими буквами.
    "Иsвtrан Ив^%ан Ива?но)вич" -> "Иванов Иван Иванович"
"""


def is_rus_char(char: str) -> bool:
    alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    return char.lower() in alf


def clean_name(fio: str) -> str:
    res = [x for x in fio if is_rus_char(x) or x == " "]
    return "".join(res)


if __name__ == "__main__":
    print(clean_name("Иsвtrан/ов Ив^%ан Ива?но)вич"))
    print(clean_name(""))
