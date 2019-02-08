from turtle import *

me = Turtle()

me.color("orange")
me.pensize(8)
me.speed(7)
me.shape("turtle")

for x in range(4):
	me.forward(100)
	me.left(90)

mainloop()