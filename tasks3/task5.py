"""
    Заполнить пропущенные значения средним арифметическим двух соседних значений.
    Например, если в 2015 году значение равно 50, в 2018 - 80,
    то в 2016 должно быть 60, в 2017 - 70
"""
yearly_sales = {
    "2015": 50,
    "2018": 65,
    "2019": 120,
    "2023": 160,
    "2025": 200
}


def fill_missed_years(ob):
    # найти промежутки меж годами и разницу между ними
    # прибавить промежуткам года
    new_ob = ob.copy()
    keys_arr = sorted(map(int, new_ob.keys()))
    print(keys_arr)
    for prev_date, next_date in zip(keys_arr, keys_arr[1:]):

        len_dates = next_date - (prev_date + 1)  # получаем количество отсутствующих дат

        if len_dates != 0: # если промежуточных дат нет пропускаем

            step = (new_ob[str(next_date)] - new_ob[str(prev_date)]) / (len_dates + 1)  # высчитываем шаг
            counter = 1
            for key in range(prev_date + 1, next_date):  # проходим по ренжу между дат

                new_ob[str(key)] = round((new_ob[str(prev_date)]) + step * counter)
                counter += 1  # для последующих увеличиваем шаг на себя же

    return dict(sorted(new_ob.items()))


if __name__ == "__main__":
    res = fill_missed_years(yearly_sales)
    print(res)

    # {
    #     "2015": 50,
    #     "2016": 55,
    #     "2017": 60,
    #     "2018": 65,
    #     "2019": 120,
    #     "2020": 130,
    #     "2021": 140,
    #     "2022": 150,
    #     "2023": 160,
    #     "2024": 180,
    #     "2025": 200
    # }
