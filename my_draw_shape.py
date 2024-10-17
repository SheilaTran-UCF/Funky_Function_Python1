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
    turtle.forward(80)
    turtle.circle(-56, 200)
    turtle.left(120)
    turtle.circle(-56, 200)
    turtle.forward(80)
    turtle.end_fill()

    # Generate new values for color, x, and y
    new_color = (max(0, min(100, color[0] + random.randint(-5, 5))), 0, 0)  # keep it in the red color range
    new_x = max(0, min(800, x + random.randint(-10, 10)))  # keep x within bounds
    new_y = max(0, min(600, y + random.randint(-10, 10)))  # keep y within bounds

    return new_color, new_x, new_y