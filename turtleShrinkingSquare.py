import turtle

turtleScreen=turtle.Screen()
turtleScreen.bgcolor("light green")
turtleScreen.title("Turtle Python")

turtleInstance= turtle.Turtle()
turtleInstance.color("white")
def ShrinkingSquare(size):
    for i in range(4):
        turtleInstance.forward(size)
        turtleInstance.left(90)
        size-=5

ShrinkingSquare(180)
ShrinkingSquare(160)
ShrinkingSquare(140)
ShrinkingSquare(120)
ShrinkingSquare(100)
ShrinkingSquare(80)
ShrinkingSquare(60)
ShrinkingSquare(40)
ShrinkingSquare(20)
turtle.done()