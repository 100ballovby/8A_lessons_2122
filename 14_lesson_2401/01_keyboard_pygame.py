import pygame as pg

BLUE = (112, 96, 204)
VIOLET = (126, 62, 138)
YELLOW = (247, 237, 121)

# создаю объект окна программы
s = pg.display.set_mode((640, 480))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

# рисуем тут

pg.display.update()
finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True
        elif event.type == pg.KEYDOWN:  # если кто-то нажал на любую кнопку
            print(f'Нажата клавиша: {event.key}')  # вывести сообщение об этом
            if event.key == pg.K_b:  # если нажали кнопку с буквой b
                s.fill(BLUE)
            elif event.key == pg.K_v:  # если нажали кнопку с буквой v
                s.fill(VIOLET)
            elif event.key == pg.K_y:  # если нажали кнопку с буквой y
                s.fill(YELLOW)
            elif event.key == pg.K_m:
                pg.font.init()  # инициализирую шрифт
                font_style = pg.font.SysFont(name='Calibri',
                                             size=30, bold=True)
                text = font_style.render('Какой-то текст', True, (255, 255, 255))
                s.blit(text, [200, 200])

    pg.display.update()

