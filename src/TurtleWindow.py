import turtle

def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("red")

    painter = turtle.Turtle()
    painter.forward(100)

    window.exitonclick()

draw_triangle()