# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
from cats import snowflake3, draw, move, get_num, remove, y

snowflake3(25)
while True:
    draw(sd.background_color)
    move()
    draw(sd.COLOR_WHITE)
    fallen_angel = get_num()
    if len(fallen_angel):
        draw(sd.background_color)
        remove(fallen_angel)
        draw(sd.COLOR_WHITE)
        snowflake3(len(fallen_angel), offset=y - 40)

    sd.sleep(0.001)

sd.pause()
