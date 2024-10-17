import turtle
from my_draw_shape import minh_draw_heart
from all_draw_shape  import all_minh_draw_heart
from all_my_draw_shape import second_minh_draw_heart

turtle.colormode(255)


def main(
    color=(255, 0, 0),  # Start with red color
    x=0,  # Starting x coordinate
    y=0, # Starting y coordinate
):
    turtle.speed(1)  # Set the drawing speed
    turtle.title("Drawing a Heart")
    # Call the draw_heart function
    new_color, new_x, new_y = minh_draw_heart(color, x, y)

    # Output the returned values
    print("New Color:", new_color)
    print("New X:", new_x)
    print("New Y:", new_y)

    new_color, new_x, new_y = second_minh_draw_heart(color, x, y)

    # Output the returned values
    print("New Color:", new_color)
    print("New X:", new_x)
    print("New Y:", new_y)

    new_color, new_x, new_y = all_minh_draw_heart(color, x-100, y)

    # Output the returned values
    print("New Color:", new_color)
    print("New X:", new_x)
    print("New Y:", new_y)

    # Finish up
    turtle.done()


if __name__ == "__main__":
    main(y=-50)  # color=(255, 0, 0), x=0, y=-50
