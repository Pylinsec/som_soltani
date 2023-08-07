from turtle import *

pensize(3)
speed(0)
pencolor('white')
bgcolor('black')
fillcolor('red') # entekhab rang
 # soroo entekhab nahieh 
for k in range(1,9):
    begin_fill()
    for i in range(4):
        fd(50)
        lt(90)
    end_fill()    # payan naheih jehat rang 
    penup()
    goto(k*50,0)  
    pendown()  



hideturtle()
done()