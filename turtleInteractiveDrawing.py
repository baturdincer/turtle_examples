import turtle

drawingBoard=turtle.Screen()
drawingBoard.bgcolor("light blue")
drawingBoard.title("Drawing Board")

turtleInstance=turtle.Turtle()

def turle_forward():
    turtleInstance.forward(100)
def turle_rotate_right():
    turtleInstance.right(90)
def turle_rotate_left():
    turtleInstance.left(90)
def clear_screen():
    turtleInstance.clear()
def return_home():
    turtleInstance.home()
def turtle_pen_up():
    turtleInstance.penup()
def turtle_pen_down():
    turtleInstance.pendown()

drawingBoard.listen()
drawingBoard.onkey(turle_forward,"w")
drawingBoard.onkey(turle_rotate_left,"a")
drawingBoard.onkey(turle_rotate_right,"d")
drawingBoard.onkey(clear_screen,"c")
drawingBoard.onkey(return_home,"space")
drawingBoard.onkey(turtle_pen_up,"g")
drawingBoard.onkey(turtle_pen_down,"h")
turtle.mainloop()