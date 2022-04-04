with open('src/pi_digits.txt') as file_obj:  # открыть файл и присвоить его в переменную file_obj
    pi_string = ''  # пустая строка для сохранения числа π
    for line in file_obj:   # контент файла теперь в переменной txt
        pi_string += line.strip()  # добавить строку из файла, убрав все пробелы
    print(f'π = {pi_string}')
    # для того, чтобы превратить содержимое файла в число
    pi_string = float(pi_string)
    print(pi_string, type(pi_string))
# file_obj.read()  <- ошибка, потому что with автоматически закрывает файл

