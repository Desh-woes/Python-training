import turtle
nmbr=input('please enter the number of sides for the shape you want to draw')
number=int(nmbr)
for steps in range(number):
    turtle.forward(20)
    turtle.right(360/number)
    for moresteps in range(number):
        turtle.forward(10)
        turtle.right(360/number)
