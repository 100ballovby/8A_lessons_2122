import pygame as pg
from pygame.draw import rect, circle, polygon

W = 640
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

img = pg.image.load('car.png').convert_alpha()  # загружаю и конвертирую
img_rect = img.get_rect()  # превращаю картинку в объект
img_rect.center = 200, 150  # центр изображения в х: 200, у: 150
car = img  # копия изображения
car_rect = img_rect  # копия объекта

angle = 0

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.fill((255, 255, 255))
    screen.blit(car, car_rect)
    pg.display.update()

    keys = pg.key.get_pressed()
    if keys[pg.K_d]:
        img_rect.x += 10
        angle = -90
    if keys[pg.K_a]:
        img_rect.x -= 10
        angle = 90
    if keys[pg.K_w]:
        img_rect.y -= 10
        angle = 0
    if keys[pg.K_s]:
        img_rect.y += 10
        angle = 180
    car = pg.transform.rotate(img, angle)

    if img_rect.right >= W:
        img_rect.right = W - 5
    elif img_rect.left <= 0:
        img_rect.left = 5
    elif img_rect.top <= 0:
        img_rect.top = 5
    elif img_rect.bottom >= H:
        img_rect.bottom = H - 5
