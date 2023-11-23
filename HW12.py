import string

user_input = input("Enter words: ")

user_input = "".join(punct for punct in user_input if punct not in string.punctuation)

words = user_input.split()
words = [word.title() for word in words]
user_input = " ".join(words)

if len(user_input) > 140:
  user_input = user_input[:139]

user_input = user_input.replace(" ", "")
user_input = "#{}".format(user_input)

print(user_input)
