import random

color = (55, 0, 0)
x = 0
y = -50

songaunhien = random.randint(-100, 100)
new_color = (max(0, min(100, color[0] + songaunhien)), 0, 0)  # keep it in the red color range
songaunhien_ = random.randint(-15, 15)
new_x = max(0, min(800, x + songaunhien_))  # keep x within bounds
songaunhien__ = random.randint(-15, 15)
new_y = max(0, min(600, y + songaunhien__))  # keep y within bounds
