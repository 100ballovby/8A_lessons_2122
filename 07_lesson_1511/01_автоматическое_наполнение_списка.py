import random as r

a = []  # пустой список
for n in range(15):  # повторить 15 раз
    r_int = r.randint(1, 100)  # генерирую число от 1 до 100
    a.append(r_int)  # и добавляю его в список

print(a)
