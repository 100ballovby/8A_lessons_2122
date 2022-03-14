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


def ball_moving(obj, s_width, s_height, plr, enm):
    """
    Функция перемещения шарика в пространстве
    :param obj: игровой объект-мяч
    :param s_width: ширина экрана
    :param s_height: высота экрана
    :param plr: ракетка-игрок
    :param enm: ракетка-оппонент
    :return: None
    """
    global ball_speed_x, ball_speed_y
    obj.x += ball_speed_x
    obj.y += ball_speed_y

    if obj.top <= 0 or obj.bottom >= s_height:
        ball_speed_y *= -1
    if obj.left <= 0 or obj.right >= s_width:
        ball_speed_x *= -1

    if obj.colliderect(plr) or obj.colliderect(enm):
        ball_speed_x *= -1


def opponent_ai(obj, s_height, enm, speed):
    """
    Искусственный интеллект платформы-оппонента.
    Если платформа находится выше шарика, нужно двигаться вниз,
    если платформа ниже шарика - вверх.
    :param obj: игровой объект-мяч
    :param s_height: высота экрана
    :param enm: платформа-оппонент
    :param speed: скорость перемещения
    :return: None
    """
    if enm.top < obj.y:  # если верхняя часть платформы выше У шарика
        enm.y += speed  # опустить платформу вверх
    if enm.bottom > obj.y:  # если нижняя часть платформы ниже У шарика
        enm.y -= speed  # поднять платформу

    if enm.top <= 0:  # если платформа зашла за верхнюю границу экрана
        enm.top = 0  # остановить ее на верхней границе
    elif enm.bottom >= s_height:  # если платформа ушла за нижнюю границу экрана
        enm.bottom = s_height  # остановить ее на нижней границе


def platform_animation(plr, speed, height):
    """
    Функция отвечает за передвижение платформы-игрока
    :param plr: Объект-игрок
    :param speed: Скорость передвижения
    :param height: Высота экрана
    :return: None
    """
    plr.y += speed

    if plr.bottom >= height:
        plr.bottom = height
    elif plr.top <= 0:
        plr.top = 0


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

# Game variables
ball_speed_x = 8
ball_speed_y = 8
opponent_speed = 8
p_speed = 0

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                p_speed -= 8
            if event.key == pg.K_DOWN:
                p_speed += 8
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                p_speed += 8
            if event.key == pg.K_DOWN:
                p_speed -= 8

    # Visuals
    screen.fill(bg_color)
    rect(screen, l_gray, platform)
    rect(screen, l_gray, opponent)
    ellipse(screen, l_gray, ball)
    aaline(screen, l_gray, [W // 2, 0], [W // 2, H])

    # Game logic
    ball_moving(ball, W, H, platform, opponent)
    opponent_ai(ball, H, opponent, opponent_speed)
    platform_animation(platform, p_speed, H)

    pg.display.update()