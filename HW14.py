user_input = int(input("Enter an integer: "))

while user_input > 9:
    digits = [int(digit) for digit in str(user_input)]

    result = 1
    for digit in digits:
        result *= digit

    user_input = result


print(user_input)

