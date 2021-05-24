import turtle

#creating an instance of turtle
flag=turtle.Turtle()

flag.speed(4) #method for animations
flag.pensize(5) #for thickness of pen
flag.color('blue') #colour of spokes

#function to define movements
def draw(x, y):
    flag.penup()
    flag.goto(x,y)
    flag.pendown()

#loop for drawing 24 spokes  
for i in range(24):
    flag.forward(80) #length of each stroke is 80
    flag.backward(80)
    flag.left(15)
draw(0, -80)

#creating circle at the edges of the spokes
flag.circle(80,360)

#green rectangle creation
flag.color('green')
flag.begin_fill()

flag.forward(350)
flag.backward(700)
flag.right(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)

flag.end_fill()

#orangeRectangle
flag.color('orange')
draw(-350,80)
flag.begin_fill()

flag.right(180)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)

flag.end_fill()

turtle.done()
