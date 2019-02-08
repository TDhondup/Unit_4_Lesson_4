from turtle import *

me = Turtle()

me.color("pink")
me.pensize(7)
me.speed(3)
me.shape("arrow")

for x in range(6):
	me.forward(100)
	me.left(60)

mainloop()