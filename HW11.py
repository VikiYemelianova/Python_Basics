message = 'You can\'t divide by 0'
while True:

    x = int(input('Please enter first number: '))
    y = int(input('Please enter second number: '))
    i = (input('Please enter action: '))

    if i == '+':
        print(f'Your result is {x+y}')
    elif i == '-':
        print(f'Your result is {x-y}')
    elif i == '*':
        print(f'Your result is {x*y}')
    elif i == '/':
        if y != 0:
            print(f'Your result is {x/y}')
        else:
            print(message)

    try_again = input('Do you want to perform another calculation? [y/n]: ')
    if try_again != 'y':
        break

