import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randrange


W = 640
H = 640
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

# настраиваю появление квадрата
x1 = W // 2  # начальные координаты появления объекта на экране
y1 = H // 2  # начальные координаты появления объекта на экране
x1_change = 0  # смена положения объекта на экране
y1_change = 0  # смена положения объекта на экране
block = 20
speed = 20

# неигровой персонаж
enemy_x = round(randrange(0, W - block) / 10) * 10
enemy_y = round(randrange(0, H - block) / 10) * 10


finished = False
while not finished:
    clock.tick(speed)  # частота обновления
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                x1_change = 0
                y1_change = -block
            elif event.key == pg.K_DOWN:
                x1_change = 0
                y1_change = block
            elif event.key == pg.K_LEFT:
                x1_change = -block
                y1_change = 0
            elif event.key == pg.K_RIGHT:
                x1_change = block
                y1_change = 0
            elif event.key == pg.K_ESCAPE:  # если нажали на esc
                x1_change = y1_change = 0  # остановить

    # рисуем тут
    screen.fill((255, 255, 255))  # заливаю экран цветом
    rect(screen, (84, 140, 214), [x1, y1, block, block])  # игровой персонаж
    rect(screen, (227, 113, 166), [enemy_x, enemy_y, block, block])
    pg.display.update()

    if x1 == enemy_x and y1 == enemy_y:
        print('HIT!')

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


