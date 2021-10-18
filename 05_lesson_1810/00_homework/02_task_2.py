n = int(input('Введите число: '))
factoreal = 1

if (n == 0) or (n == 1):
    print(f'{n}! = {factoreal}')
else:
    for number in range(1, n + 1):
        factoreal *= number
    print(f'{n}! = {factoreal}')

