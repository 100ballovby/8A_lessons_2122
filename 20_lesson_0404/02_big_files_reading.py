with open('src/pi_million_digits.txt') as file_obj:  # открыть файл и присвоить его в переменную file_obj
    pi_string = ''
    for line in file_obj:
        pi_string += line.strip()
    print(pi_string[:52])  # вывести число π до 50 знака (после запятой) включительно
    print(len(pi_string))
