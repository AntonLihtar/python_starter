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
    keys_arr = list(yearly_sales.keys())  # преобразуем в список дат
    for index in range(len(keys_arr) - 1):  # индексы значений
        prev_date = int(keys_arr[index]) + 1
        next_date = int(keys_arr[index + 1])

        len_dates = next_date - prev_date  # получаем количество отсутствующих дат
        if len_dates == 0:
            continue
        step = (new_ob[keys_arr[index + 1]] - new_ob[keys_arr[index]]) / (len_dates + 1)  # высчитываем шаг
        counter = 1
        for key in range(prev_date, next_date):  # проходим по ренжу между дат
            new_ob[str(key)] = int(new_ob[keys_arr[index]] + step * counter)
            counter += 1 # для последующих увеличиваем шаг на себя же

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
