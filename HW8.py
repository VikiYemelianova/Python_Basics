lst = [1, 3, 5]
summa = sum(lst[::2])
if len(lst) == 0:
    result = 0
else:
    result = summa * lst[-1]

print(result)

