from turtle import *

pensize(3)
speed(0)
x = 0
y = 0

for k in range(8):
    # make row ba 8 morabba 
    for j in range(8):
        # make morabba
        if (j+k)%2 == 0:
            fillcolor('black')
        else:
            fillcolor('white')    
        begin_fill()    
        for i in range(4):
            fd(60)
            rt(90)
        end_fill()
        fd(60) 
        # penup()
        # x += 60
        # goto(x,y)   
        # pendown()
    penup()
    y -= 60
    x = 0
    goto(0,y)   
    pendown()    

done()