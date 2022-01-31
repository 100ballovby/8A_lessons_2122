import pygame as pg
from pygame.draw import rect, circle, polygon

W = 640
H = 640
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

# настраиваю появление квадрата
x1 = W // 3  # начальные координаты появления объекта на экране
y1 = H // 2  # начальные координаты появления объекта на экране
x1_change = 0  # смена положения объекта на экране
y1_change = 0  # смена положения объекта на экране


finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                x1_change = 0
                y1_change = -5
            elif event.key == pg.K_DOWN:
                x1_change = 0
                y1_change = 5
            elif event.key == pg.K_LEFT:
                x1_change = -5
                y1_change = 0
            elif event.key == pg.K_RIGHT:
                x1_change = 5
                y1_change = 0
            elif event.key == pg.K_ESCAPE:  # если нажали на esc
                x1_change = y1_change = 0  # остановить

    # рисуем тут
    screen.fill((255, 255, 255))  # заливаю экран цветом
    rect(screen, (84, 140, 214), [x1, y1, 50, 50])
    pg.display.update()

    x1 += x1_change
    y1 += y1_change

    if x1 >= W:
        x1 = 0
    elif x1 < 0:
        x1 = W
    elif y1 >= H:
        y1 = 0
    elif y1 < 0:
        y1 = H


