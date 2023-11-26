import string
user_input = input("Enter letters: ")

letters = user_input.split('-')
print(letters)
min_let, max_let = min(letters[0], letters[1]), max(letters[0], letters[1])

if max_let.isupper():
    result = "".join([let for let in string.ascii_uppercase if min_let <= let.upper() <= max_let])
else:
    result = "".join([let for let in string.ascii_lowercase if min_let <= let <= max_let])

print(result)

#?????

