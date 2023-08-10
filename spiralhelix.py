import turtle

turtleScreen= turtle.Screen()
turtleScreen.bgcolor("cyan")
turtleScreen.title("Python Turtle")

turtleInstance=turtle.Turtle()
turtleInstance.color("blue")

colorsList=["blue", "yellow", "green", "cyan", "pink", "purple", "red", "light green", "grey", "white"]

for i in range(10):
    turtleScreen.bgcolor(colorsList[i])
    turtleInstance.circle(10*i)
    turtleInstance.circle(-10*i)
    turtleInstance.left(i)
turtle.done()