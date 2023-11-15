num = int(input('Enter a 5-digit number: '))

a = (num // 10000)
num = num % 10000

b = (num // 1000)
num = num % 1000

c = (num // 100)
num = num % 100

d = (num // 10)
num = num % 10

e = (num // 1)
num = num % 1

print(e, d, c, b, a)