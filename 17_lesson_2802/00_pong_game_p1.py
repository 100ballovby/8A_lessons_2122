import pygame as pg
from pygame.draw import rect, circle, polygon


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


W = 640
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    pg.display.update()