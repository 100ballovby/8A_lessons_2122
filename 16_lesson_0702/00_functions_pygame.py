import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randint


def show_message(msg, color, surface, font_name, x, y):
    """
    Функция отображает текст на экране в определенном месте
    :param msg: текст сообщения
    :param color: цвет текста
    :param surface: поверхность, на которой пишем
    :param font_name: имя шрифта (начертание)
    :param x: координата х для шрифта
    :param y: координата y для шрифта
    :return: None
    """
    pg.font.init()  # инициализирую шрифт
    font_style = pg.font.SysFont(font_name, 20, True)  # стиль шрифта
    text = font_style.render(msg, True, color)  # отобразить текст и задать ему цвет
    surface.blit(text, [x, y])  # показать на экране в определенных координатах


W = 640
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

block = 50
x = W // 2 - block // 2
y = H // 2 - block // 2
x_change = 0
y_change = 0

food_x = randint(0, W - block)
food_y = randint(0, H - block)

score = 0

finished = False
while not finished:
    clock.tick(15)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                score += 1
            if event.key == pg.K_LEFT:
                x_change = -block
                y_change = 0
            if event.key == pg.K_RIGHT:
                x_change = block
                y_change = 0
            if event.key == pg.K_UP:
                x_change = 0
                y_change = -block
            if event.key == pg.K_DOWN:
                x_change = 0
                y_change = block

    screen.fill(WHITE)

    player = rect(screen, RED, [x, y, block, block])
    enemy = rect(screen, BLUE, [food_x, food_y, block, block])

    x += x_change
    y += y_change

    if player.colliderect(enemy):  # если player коснулся enemy
        score += 1
        food_x = randint(0, W - block)
        food_y = randint(0, H - block)

    if (player.x < 0 or player.x >= W) or (player.y < 0 or player.y >= H):
        finished = True

    show_message(f'Score: {score}', BLACK, screen,
                 'comicsans', 0, 0)

    pg.display.update()




