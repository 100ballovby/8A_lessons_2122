import pygame as pg
from pygame.draw import rect, circle, polygon, ellipse

# создаю объект окна программы
s = pg.display.set_mode((640, 480))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

# нарисуем прямоугольник
rect(s, (207, 124, 207), [150, 150, 100, 70])
# поверхность, (цвет), [x, y, ширина, высота]
rect(s, (255, 182, 173), [145, 145, 110, 80], 5)
# поверхность, (цвет), [x, y, ширина, высота], толщина_обводки

# нарисуем круг
circle(s, (255, 165, 138), [400, 250], 100)
circle(s, (125, 196, 250), [560, 370], 60, 5)
# поверхность, (цвет), [x, y], диаметр, толщина_обводки

# нарисуем несколько квадратов
for i in range(7):
    rect(s, (51, 204, 255), [55 * i, 310, 50, 50], 5)

# нарисуем треугольник
polygon(s, (14, 104, 143), [[450, 140], [540, 20], [630, 140]], 4)
# пятиугольник
polygon(s, (14, 104, 143), [[450, 140], [470, 120], [490, 140],
                            [480, 160], [460, 160]], 4)
# эллипс
ellipse(s, (248, 0, 0), [10, 50, 190, 70])

pg.display.update()
finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

