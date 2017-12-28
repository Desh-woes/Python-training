import turtle
nmbr=int(input('please enter the lenght of the line you want to draw'))
ang= int(input('pleasde enter the angle of the object you want to draw'))
colour= input('please enter the color of pen you want i.e blue, red, green')
while nmbr != 0 :
    turtle.color(colour)
    turtle.forward(nmbr)
    turtle.right(ang)
    nmbr= int(input('please enter the length of the line you want to draw'))
    if nmbr != 0:
        ang= int(input('please enter the angle of the object you want to draw'))
        colour= input('please enter the color of pen you want i.e blue, red, green')
