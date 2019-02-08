from turtle import *

me = Turtle()
kennethchan = Turtle()

me.color("red")
me.pensize(6)
me.speed(7)
me.shape("triangle")

kennethchan.color("blue")
kennethchan.pensize(6)
kennethchan.speed(9)
kennethchan.shape("circle")

for x in range(3):
	me.forward(100)
	me.left(120)

kennethchan.circle(50)

mainloop()

