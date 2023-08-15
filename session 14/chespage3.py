from turtle import *

pensize(3)
speed(0)
x = -300
y = 300
penup()
goto(x,y)
pendown()

for k in range(8):
    # make row ba 8 morabba 
    for j in range(8):
        if (j+k)%2 == 0:
            fillcolor('yellow')
        else:
            fillcolor('green')    
        begin_fill()    
        # make morabba
        # for i in range(4):
        #     fd(60)
        #     rt(90)
        circle(40)
        write('som')
        end_fill()
        # fd(60) 
        penup()
        y -= 80
        goto(x,y)   
        pendown()
    penup()
    y = 300
    x += 80
    goto(x,y)   
    pendown()    

done()