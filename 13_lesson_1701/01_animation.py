import pygame as pg
from pygame.draw import circle, polygon
import time

WIN_WIDTH = 640
WIN_HEIGHT = 480
WHITE = (255, 255, 255)
RED = (230, 44, 44)
GREEN = (8, 199, 84)

# настрою круг
rad = 50
cir_x = 0 - rad  # скрываю круг за левой границей экрана
cir_y = WIN_HEIGHT / 2  # ставлю его посередине

# настрою треугольник
pol_x = 0 - 100
pol_y = WIN_HEIGHT / 3

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

    s.fill((255, 255, 255))  # заливаю экран белым цветом
    # рисуем круг
    circle(s, RED, (cir_x, cir_y), rad)

    # рисуем треугольник
    polygon(s, GREEN, [[pol_x, pol_y],
                       [pol_x, pol_y + 110],
                       [pol_x + 100, pol_y + 55]])

    pg.display.update()  # обновляю кадры внутри цикла

    # если круг оказался за пределами правой части экрана
    if cir_x > WIN_WIDTH + rad:
        cir_x = 0 - rad  # переместить его влево
    elif pol_x > WIN_WIDTH:
        time.sleep(2)
        pol_x = 0 - 100
    else:
        cir_x += 2  # изменяю х круга
        pol_x += 5
