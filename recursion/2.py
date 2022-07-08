import turtle

MAX_LENGTH = 240
INCREMENT = 10


def draw_spiral(a_turtle, line_length):
    if line_length > MAX_LENGTH:
        return
    a_turtle.forward(line_length)
