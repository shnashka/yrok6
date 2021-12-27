# -*- coding: utf-8 -*-

import simple_draw as sd
import random as r

x = 1000
y = 1000
sd.resolution = (x, y)
_snowflakes = []


def snowflake3(N, offset=0):
    for _ in range(N):
        snowflake = [r.randint(0, x), r.randint(offset, y), r.randint(10, 100)]

        _snowflakes.append(snowflake)


def move():
    for i in range(len(_snowflakes)):
        if _snowflakes[i][1] > 30:
            _snowflakes[i][0] += r.randint(-15, 15)
            _snowflakes[i][1] -= r.randint(0, 15)


def draw(color):
    for snowflakes in _snowflakes:
        point = sd.get_point(snowflakes[0], snowflakes[1])
        sd.snowflake(center=point, length=snowflakes[2], color=color)


def remove(nums):
    for num in nums:
        _snowflakes.pop(num)


def get_num():
    result = []
    for i in range(len(_snowflakes)):
        if _snowflakes[i][1] <= 50:
            result.append(i)
    return result
