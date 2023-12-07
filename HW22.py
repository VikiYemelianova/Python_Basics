def difference(*numbers):
    if not numbers:
        return 0

    max_num = -float('inf')
    min_num = float('inf')

    for number in numbers:
        if number > max_num:
            max_num = number
        if number < min_num and number != -float('inf'):
            min_num = number

    return round(max_num - min_num, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')