import turtle

def draw():

    window = turtle.Screen()
    window.bgcolor("red")

    # draw square
    shape1 = turtle.Turtle()
    # customize square
    shape1.shape("arrow")
    shape1.color("white")

    # loop to draw 4 lines of square
    for i in range(4):
        shape1.forward(100)
        shape1.right(90)

    # draw circle
    shape3 = turtle.Turtle()
    # customize circle
    shape3.shape("turtle")
    shape3.color("yellow")
    shape3.circle(100)

    # draw triangle
    shape3 = turtle.Turtle()
    # customize triangle
    shape3.shape("turtle")
    shape3.color("black")

    for i in range(2):
        shape3.forward(100)
        shape3.right(120)
    shape3.forward(100)


    window.exitonclick()

draw()
