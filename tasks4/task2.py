def contains_in_list(small: list[int], big: list[int]) -> bool:
    """
        Выведите true, если массив содержится в другом массиве
        в том же порядке. Не обязательно элементы должны идти один
        за другим.

        contains_in_list([3, 4, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == true
        Темы: списки
    """
    res_index = 0
    for el in small:
        if el not in big[res_index:]:
            return False
        else:
            ind = big.index(el, res_index)
            if ind < res_index:
                return False
            res_index = ind + 1
    return True


if __name__ == "__main__":
    print(contains_in_list([3, 4, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(contains_in_list([8, 4, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
