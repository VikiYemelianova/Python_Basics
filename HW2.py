num = int(input('Enter a 4-digit number from 0 to 9 including: '))

print(num // 1000)
num = num % 1000

print(num // 100)
num = num % 100

print(num // 10)
num = num % 10

print(num)

