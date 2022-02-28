import pygame as pg
from pygame.draw import rect, ellipse, aaline
from random import randint


def show_message(txt, color, x, y, size):
    """
    Функци для отображения текста в игре.
    :param txt: Текст для отображения
    :param color: Цвет текста
    :param x: координаты
    :param y: координаты
    :param size: размер шрифта
    :return: None
    """
    pg.font.init()
    font = pg.font.SysFont('comicsans', size)
    msg = font.render(txt, True, color)
    screen.blit(msg, [x, y])


W = 1280
H = 960
screen = pg.display.set_mode((W, H))
pg.display.set_caption('Pong game v1🏓')
clock = pg.time.Clock()

# Colors
l_gray = (200, 200, 200)
bg_color = (107, 107, 107)

# Game objects
ball = pg.Rect(W // 2 - 15, H // 2 - 15, 30, 30)
platform = pg.Rect(W - 20, H // 2, 10, 150)
opponent = pg.Rect(10, H // 2, 10, 150)

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    # Visuals
    screen.fill(bg_color)
    rect(screen, l_gray, platform)
    rect(screen, l_gray, opponent)
    ellipse(screen, l_gray, ball)
    aaline(screen, l_gray, [W // 2, 0], [W // 2, H])

    pg.display.update()