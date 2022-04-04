with open('src/pi_digits.txt') as file_obj:  # открыть файл и присвоить его в переменную file_obj
    txt = file_obj.read()   # контент файла теперь в переменной txt
    print(txt)

# file_obj.read()  <- ошибка, потому что with автоматически закрывает файл

