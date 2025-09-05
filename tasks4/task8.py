def reverse_words(input_str: str) -> str:
    """
        Написать функцию, которая принимает предложение и возвращает
        строка со словами из исходного предложения в обратном порядке.
        actual = reverse_words("the sky is blue") == "blue is sky the"
        Темы: парсинг строк
    """
    # Разбиваем строку на слова и переворачиваем список
    words = input_str.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


if __name__ == "__main__":
    res = reverse_words("the sky is blue")
    print(res)
