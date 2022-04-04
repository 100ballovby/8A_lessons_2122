with open('src/pi_million_digits.txt') as file_obj:  # открыть файл и присвоить его в переменную file_obj
    pi_string = ''
    for line in file_obj:
        pi_string += line.strip()
    birthday = input('Впиши дату рождения в формате ДДММГГ: ')

    if birthday in pi_string:  # если дата рождения есть в числе π
        print('Дата рождения найдена в числе π!')
    else:
        print('Вашей даты рождения нет в числе π!')
