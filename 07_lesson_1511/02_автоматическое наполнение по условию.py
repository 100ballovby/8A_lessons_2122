import random as r

array = []

# for i in range(10):  <- цикл for работает СТРОГО 10 раз и не будет делать дополнительные повторения
while len(array) <= 10:  # пока длина списка меньше 10
    r_int = r.randint(1, 20)  # генерирую число
    if r_int % 2 == 0:  # если число делится на 2
        array.append(r_int)  # добавить его в список

print(array)


