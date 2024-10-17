import random
import turtle

def all_minh_draw_heart(color, x, y):
    # Starting a Working Screen
    # ws = turtle.Screen()

    # initializing a turtle instance
    tur = turtle.Turtle()
    tur.color('')
    tur.goto(x, y)

    tur.color("red", "yellow")
    tur.begin_fill()
    # executing loop 5 times for a star
    for i in range(5):
        # moving turtle 100 units forward
        tur.forward(110)

        # rotating turtle 144 degree right
        tur.right(144)

    tur.end_fill()
    turtle.done()

    # Generate new values for color, x, and y
    new_color = (max(0, min(100, color[0] + random.randint(-5, 5))), 0, 0)  # keep it in the red color range
    new_x = max(0, min(800, x + random.randint(-10, 10)))  # keep x within bounds
    new_y = max(0, min(600, y + random.randint(-10, 10)))  # keep y within bounds

    return new_color, new_x, new_y


