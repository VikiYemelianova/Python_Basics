first_lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
new_lst = []
for i in first_lst:
    if i != 0:
        new_lst.append(i)
new_lst += [0] * (len(first_lst) - len(new_lst))

print(new_lst)
