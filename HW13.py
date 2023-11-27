import string
user_input = input("Enter letters: ")

first_letter, second_letter = user_input.split('-')

if (first_letter.islower() and second_letter.isupper()) or (first_letter.isupper() and second_letter.islower()):
    first_index = string.ascii_letters.index(first_letter)
    second_index = string.ascii_letters.index(second_letter)

    result = string.ascii_letters[first_index:second_index + 1]

    print(result)
else:
    first_index = string.ascii_letters.index(first_letter)
    second_index = string.ascii_letters.index(second_letter)

    result = string.ascii_letters[first_index:second_index + 1]

    print(result)

