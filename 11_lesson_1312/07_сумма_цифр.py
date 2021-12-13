from random import randint

number = randint(1, 10000)
summ = 0
mult = 1
print(number)

while number > 0:
    if number % 10 != 0:
        summ += number % 10
        mult *= number % 10
    number //= 10

print(summ)
print(mult)