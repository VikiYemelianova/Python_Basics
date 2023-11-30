import string
def is_palindrome(text):
    text = text.lower()
    text = "".join(punct for punct in text if punct not in string.punctuation)
    text = text.strip()
    text = text.replace(' ', '')
    changed_text = text[::-1]
    return text == changed_text


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

