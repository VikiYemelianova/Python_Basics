message = 'You can\'t divide by 0'
x = int(input('Please enter first number: '))
y = int(input('Please enter second number: '))
i = (input('Please enter action: '))

if i == '+':
    print(x+y)
elif i == '-':
    print(x-y)
elif i == '*':
    print(x*y)
elif i == '/':
    if y != 0:
        print(x/y)
    else:
        print(message)


