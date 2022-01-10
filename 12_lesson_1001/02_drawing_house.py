import pygame as pg
from pygame.draw import rect, circle, polygon, ellipse

# создаю объект окна программы
s = pg.display.set_mode((640, 480))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

pg.display.update()
finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

    s.fill((219, 239, 255))  # заливаю фон цветом
    # земля
    rect(s, (51, 252, 40), [0, 260, 640, 220])
    # основание дома
    rect(s, (209, 132, 96), [105, 140, 250, 200])
    # крыша
    polygon(s, (148, 93, 11), [[80, 150], [227.5, 60], [375, 150]])
    # дверь
    rect(s, (148, 93, 11), [160, 250, 50, 90])
    circle(s, (255, 215, 0), [195, 290], 5)  # ручка

    pg.display.flip()  # обновляю кадры в цикле

