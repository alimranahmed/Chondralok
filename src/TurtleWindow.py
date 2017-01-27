import turtle


def draw_square(turtle_painter):
    turtle_painter.color("green")

    for i in range(1, 5):
        turtle_painter.forward(100)
        turtle_painter.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    turtle_painter = turtle.Turtle()
    turtle_painter.shape("turtle")

    for i in range(1, 37):
        draw_square(turtle_painter)
        turtle_painter.right(10)

    draw_circle(turtle_painter)

    window.exitonclick()


def draw_circle(turtle_painter):
    turtle_painter.color("blue")
    turtle_painter.circle(100)

draw_art()
