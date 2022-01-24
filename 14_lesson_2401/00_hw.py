import pygame as pg
from pygame.draw import circle, polygon, rect
import time

WIN_WIDTH = 640
WIN_HEIGHT = 480

# настрою круг
rad = 50
cir_x = 0 - rad  # скрываю круг за левой границей экрана
cir_y = 70  # ставлю его посередине

BG = (219, 239, 255)
GROUND = (51, 252, 40)
SUN = (255, 229, 3)
DARK_BG = (5, 10, 107)
WINDOW = (26, 95, 182)

# создаю объект окна программы
s = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

pg.display.update()
finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

    s.fill(BG)  # заливаю фон цветом

    # солнце
    circle(s, SUN, [cir_x, cir_y], rad)

    # земля
    rect(s, GROUND, [0, 260, 640, 220])

    # основание дома
    rect(s, (209, 132, 96), [105, 140, 250, 200])

    # крыша
    polygon(s, (148, 93, 11), [[80, 150], [227.5, 60], [375, 150]])
    # дверь
    rect(s, (148, 93, 11), [160, 250, 50, 90])
    circle(s, (255, 215, 0), [195, 290], 5)  # ручка

    # елка
    tree_x = 450
    tree_y = 200

    for triangle in range(3):
        polygon(s, (26, 182, 26), [[tree_x, tree_y], [tree_x + 120, tree_y], [tree_x + 60, tree_y - 90]])
        tree_y += 60

    # окно
    rect(s, (122, 54, 23), [245, 245, 90, 50], 5)
    rect(s, WINDOW, [250, 250, 80, 40])

    if cir_x > WIN_WIDTH + rad:
        BG = (5, 10, 107)
        GROUND = (26, 79, 33)
        WINDOW = (255, 221, 0)

    else:
        cir_x += 5

    pg.display.flip()  # обновляю кадры в цикле


