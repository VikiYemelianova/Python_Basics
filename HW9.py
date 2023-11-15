import random
lst = []
new_lst = []

for i in range(random.randint(3, 10)):
    lst.append(random.randint(3, 10))
print(lst)
numbers = (lst[0], lst[2], lst[-2])
new_lst.extend(numbers)
print(new_lst)
