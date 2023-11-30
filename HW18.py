def common_elements():
    set_1 = {3, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63}
    set_2 = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70}

    common = set_1.intersection(set_2)
    return common

print(common_elements())



