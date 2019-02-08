from turtle import *

me = Turtle()

me.color("yellow")
me.pensize(6)
me.speed(7)
me.shape("classic")

screen = Screen()
screen.bgcolor("purple")

me.forward(200)
for x in range(3):
	me.forward(100)
	me.left(120)

me.right(90)
me.forward(200)
me.circle(50)


mainloop()