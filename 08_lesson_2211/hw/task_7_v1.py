array = [1, 34, 0, 0, 20, 6, 0, 9, 3, 1, 0, 5, 9, 19, 0]
mid = 0

for element in array:  # перебирать каждый элемент массива
    mid += element  # добавлять его к переменной

mid = mid / len(array)
print(f'Среднее арифметическое: {mid / len(array)}')
# среднее арифметическое (вар. 1)

for index in range(len(array)):  # перебираю элементы по индексам
    if array[index] == 0:  # если элемент равен 0
        array[index] = mid

print(array)

