s = [100, None, 200, 50, 150, 0, 200]

arr_tp = zip(s, s[1:])

for x1, x2 in arr_tp:
    if x1 in (0, None) or x2 in (0, None):
        print(None)
    else:
        print(x2 / x1 * 100 - 100)

print(arr_tp)