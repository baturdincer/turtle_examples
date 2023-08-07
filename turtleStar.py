import math
import turtle

r2p=180/math.pi

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")
length=50

turtle_instance= turtle.Turtle()
turtle_instance.forward(3*length)
turtle_instance.left(r2p*math.atan(3))
turtle_instance.forward(math.sqrt(10)*length)
turtle_instance.left(180+(2*r2p*math.atan(1/3)))
turtle_instance.forward(math.sqrt(10)*length)
turtle_instance.left(r2p*math.atan(3))
turtle_instance.forward(3*length)
turtle_instance.right(90+(r2p*math.atan(2/3)))
turtle_instance.forward(math.sqrt(13)*length)
turtle_instance.left(r2p*(math.atan(2/3)+math.atan(1/3)))
turtle_instance.forward(math.sqrt(10)*length)
turtle_instance.right(90+(r2p)*(math.atan(2/3)+math.atan(1/3)))
turtle_instance.forward(length*math.sqrt(13))
turtle_instance.left(r2p*2*math.atan(2/3))
turtle_instance.forward(length*math.sqrt(13))
turtle_instance.right(90+(r2p)*(math.atan(2/3)+math.atan(1/3)))
turtle_instance.forward(length*math.sqrt(10))
turtle_instance.left(r2p*(math.atan(2/3)+math.atan(1/3)))
turtle_instance.forward(math.sqrt(13)*length)

turtle.done()

