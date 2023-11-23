import string
import keyword
users_variable = input("Enter the name of the variable: ")


if users_variable[0].isdigit() or users_variable in keyword.kwlist:
    print(False)
else:
    inv_letter = False
    for letter in users_variable:
        if letter.isupper() or letter.isspace() or (letter in string.punctuation and letter != '_'):
            inv_letter = True
            break

    if inv_letter:
        print(False)
    else:
        print(True)













