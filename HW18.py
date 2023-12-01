def common_elements():
    set_1 = set(range(3, 100, 3))
    set_2 = set(range(5, 100, 5))


    common = set_1.intersection(set_2)
    return common

print(common_elements())





