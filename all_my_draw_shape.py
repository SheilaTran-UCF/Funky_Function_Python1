import random
import turtle

def second_minh_draw_heart(color, x, y):
    tur = turtle.Turtle()
    tur.speed(20)
    tur.color("red", "orange")
    tur.goto(x, y)
    tur.begin_fill()

    for i in range(50):
        tur.forward(150)
        tur.left(170)

    tur.end_fill()

    # Generate new values for color, x, and y
    new_color = (max(0, min(100, color[0] + random.randint(-100, 100))), 0, 0)  # keep it in the red color range
    new_x = max(0, min(800, x + random.randint(-15, 15)))  # keep x within bounds
    new_y = max(0, min(600, y + random.randint(-15, 15)))  # keep y within bounds

    return new_color, new_x, new_y