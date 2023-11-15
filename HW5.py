lst = []
new_lst = []
if lst:
    if len(lst) % 2 == 0:
        first_lst = lst[:len(lst)//2]
        second_lst = lst[len(lst)//2:]
    else:
        first_lst = lst[:len(lst)//2+1]
        second_lst = lst[len(lst)//2+1:]

    new_lst.append(first_lst)
    new_lst.append(second_lst)
else:
    new_lst = [[], []]

print(new_lst)
