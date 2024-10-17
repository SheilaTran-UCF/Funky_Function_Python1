import random
import turtle

def minh_draw_heart(color, x, y):
    # Set the color for the heart
    turtle.color(color)

    # Move to the specified coordinates
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Start drawing the heart shape
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(160)
    turtle.circle(-56, 200)
    turtle.left(120)
    turtle.circle(-56, 200)
    turtle.forward(160)
    turtle.end_fill()
    turtle.hideturtle()

    # Generate new values for color, x, and y
    new_color = (max(0, min(100, color[0] + random.randint(-5, 5))), 0, 0)  # keep it in the red color range
    new_x = max(0, min(800, x + random.randint(-10, 10)))  # keep x within bounds
    new_y = max(0, min(600, y + random.randint(-10, 10)))  # keep y within bounds

    return new_color, new_x, new_y


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
    tur.hideturtle()
    turtle.done()

    # Generate new values for color, x, and y
    new_color = (max(0, min(100, color[0] + random.randint(-5, 5))), 0, 0)  # keep it in the red color range
    new_x = max(0, min(800, x + random.randint(-10, 10)))  # keep x within bounds
    new_y = max(0, min(600, y + random.randint(-10, 10)))  # keep y within bounds

    return new_color, new_x, new_y


def second_minh_draw_heart(color, x, y):
    tur = turtle.Turtle()
    tur.speed(20)
    tur.color('')

    tur.goto(x, y)
    tur.color("red", "orange")
    tur.begin_fill()

    for i in range(50):
        tur.forward(150)
        tur.left(170)

    tur.end_fill()
    tur.hideturtle()

    # Generate new values for color, x, and y
    new_color = (max(0, min(100, color[0] + random.randint(-100, 100))), 0, 0)  # keep it in the red color range
    new_x = max(0, min(800, x + random.randint(-15, 15)))  # keep x within bounds
    new_y = max(0, min(600, y + random.randint(-15, 15)))  # keep y within bounds

    return new_color, new_x, new_y