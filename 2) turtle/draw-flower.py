import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")

    # Create the turtle shape1 - Draws a square
    shape1 = turtle.Turtle()
    shape1.shape("turtle")
    shape1.color("yellow")
    shape1.speed(13)

    # Draw circle by squares "flower"
    for i in range(56):
        draw_square(shape1)
        shape1.right(8)

    shape1.forward(350)

    window.exitonclick()

draw_art()
