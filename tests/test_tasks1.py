import pytest
from tasks1.task1 import is_odd
from tasks1.task2 import is_prime
from tasks1.task3 import is_arifm_progression
from tasks1.task4 import get_triangle_kind
from tasks1.task5 import is_palindrom, is_palindrom2
from tasks1.task6 import get_words
from tasks1.task7 import get_person_short_name
from tasks1.task8 import is_list_growing
from tasks1.task9 import get_pairs_number


def test_task1():
    assert is_odd(1) == False
    assert is_odd(4) == True
    assert is_odd(7) == False
    assert is_odd(0) == True
    assert is_odd(-11) == False
    assert is_odd(-2) == True


def test_task2():
    assert is_prime(20) == False
    assert is_prime(-5) == False
    assert is_prime(7) == True
    assert is_prime(3) == True
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(42) == False


def test_task3():
    assert is_arifm_progression(1, 2, 3) == True
    assert is_arifm_progression(10, 5, 0) == True
    assert is_arifm_progression(1, 2, 4) == False
    assert is_arifm_progression(5, 5, 5) == True
    assert is_arifm_progression(-3, 0, 3) == True
    assert is_arifm_progression(-1, 0, 2) == False
    assert is_arifm_progression(100, 200, 300) == True


def test_task4():
    assert get_triangle_kind(180, 3, 3) == "некорректные значения"
    assert get_triangle_kind(60, 60, 60) == "равносторонний"
    assert get_triangle_kind(100, 40, 40) == "равнобедренный"
    assert get_triangle_kind(-20, 180, 20) == "некорректные значения"
    assert get_triangle_kind(30, 70, 80) == "обычный"


def test_task5():
    assert is_palindrom("казак") == True
    assert is_palindrom2("казак") == True
    assert is_palindrom("а роза упала на лапу азора") == True
    assert is_palindrom2("а роза упала на лапу азора") == True
    assert is_palindrom("привет") == False
    assert is_palindrom2("привет") == False
    assert is_palindrom("А роза упала на лапу Азора") == True
    assert is_palindrom2("А роза упала на лапу Азора") == True
    assert is_palindrom("") == True
    assert is_palindrom2("") == True
    assert is_palindrom("а") == True
    assert is_palindrom2("а") == True
    assert is_palindrom("   ") == True
    assert is_palindrom2("   ") == True


def test_task6():
    assert get_words("Александр Сергеевич Пушкин") == ["Александр", "Сергеевич", "Пушкин"]
    assert get_words("Привет") == ["Привет"]
    assert get_words("") == []
    assert get_words("один два три четыре") == ["один", "два", "три", "четыре"]
    assert get_words("  начало середина конец  ") == ["начало", "середина", "конец"]
    assert get_words("слово    другое") == ["слово", "другое"]
    assert get_words("   ") == []


def test_task7():
    assert get_person_short_name("Лермонтов Михаил Юрьевич") == "Лермонтов М. Ю."
    assert get_person_short_name("лермонтов михаил юрьевич") == "Лермонтов М. Ю."
    assert get_person_short_name("  Лермонтов   Михаил   Юрьевич  ") == "Лермонтов М. Ю."
    assert get_person_short_name("Иванов Анна Петровна") == "Иванов А. П."
    # Тест 5: Одно слово (граничный случай)
    assert get_person_short_name("тест") == "Тест"
    # Тест 6: Два слова (граничный случай)
    assert get_person_short_name("дон Педро") == "Дон П."


def test_task8():
    assert is_list_growing([1, 2, 3, 4, 5]) == True
    assert is_list_growing([1, 2, 2, 4, 5]) == False
    assert is_list_growing([5, 4, 3, 2, 1]) == False
    assert is_list_growing([]) == True
    assert is_list_growing([42]) == True
    assert is_list_growing([1, 2]) == True
    assert is_list_growing([2, 1]) == False


def test_task9():
    assert get_pairs_number([1, 2, 3, 4], 3) == [(1, 2)]
    assert get_pairs_number([1, 1, 1, 1], 5) == []
    assert get_pairs_number([], 5) == []
    assert get_pairs_number([5], 10) == []
    assert get_pairs_number([2, 3], 5) == [(2, 3)]
    assert get_pairs_number([2, 6, 4, 6, 1, 9], 10) == [(6, 4), (4, 6), (1, 9)]
