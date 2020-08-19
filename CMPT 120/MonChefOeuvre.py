#Mon Chef-dâ€™Oeuvre
#My Program draws the perspective of someone looking at the front of a ball pit!
#Created by Jasper Quan
#July 6, 2017


import turtle as t
import random as r

def ball(numberofBalls):
    for count in range(numberofBalls):
        t.pu()
        x_pos = r.randint(-340,340)
        y_pos = r.randint(-300,100)
        while (x_pos < -250 or x_pos > 250) and y_pos>-10: #Makes sure the balls dont go too far out of the ball pit
            x_pos = r.randint(-300,300)
        t.setpos(x_pos,y_pos)
        t.colormode(255)
        ballColor = (r.randint(0,255),r.randint(0,255),r.randint(0,255)) #randomely generate colors for the balls
        t.fillcolor(ballColor)
        t.begin_fill()
        t.circle(12)
        t.end_fill()
    return

def backBallPit(length,width,color):
    t.pu()
    t.setpos(-300,225)
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    for x in range(2):
        t.fd(length)
        t.rt(90)
        t.fd(width)
        t.rt(90)
    t.end_fill()
    return

def leftBallPit(length,width,color):
    t.pu()
    t.setpos(-300,125)
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    t.rt(110)
    t.fd(length)
    t.lt(110)
    t.fd(width)
    t.lt(70)
    t.fd(length)
    t.lt(110)
    t.fd(width)
    t.end_fill()
    return

def rightBallPit(length,width,color):
    t.pu()
    t.setpos(300,125)
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    t.lt(110)
    t.fd(length)
    t.rt(110)
    t.fd(width)
    t.rt(70)
    t.fd(length)
    t.rt(110)
    t.fd(width)
    t.end_fill()
    return

def bottomBallPit(length1,length2,width,color):
    t.pu()
    t.setpos(471.01,-344.85)
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    t.lt(110)
    t.fd(width)
    t.lt(70)
    t.fd(length1)
    t.lt(70)
    t.fd(width)
    t.lt(110)
    t.fd(length2)
    t.end_fill()
    return

def square(length,color):
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    for count in range(4):
        t.fd(length)
        t.rt(90)
    t.end_fill()   
    t.pu()
    return
        

def window(length,xpos,ypos):
    t.pu()
    t.setpos(xpos,ypos)
    square(length,windowFrame_color)
    t.setpos(xpos+10,ypos-10)
    square((length-30)/2,"white")
    t.setpos(xpos+80,ypos-10)
    square((length-30)/2,"white")
    t.setpos(xpos+10,ypos-80)
    square((length-30)/2,"white")
    t.setpos(xpos+80,ypos-80)
    square((length-30)/2,"white")
    return

def background(xpos,ypos,color):
    x = xpos
    while ypos > 150:
        t.pu()
        t.setpos(x,ypos)
        t.pd()
        length = r.randint(50,100)
        t.fillcolor(color)
        t.begin_fill()
        for sides in range(2):
            t.fd(length)
            t.rt(90)
            t.fd(50)
            t.rt(90)
        t.end_fill()
        x += length
        if x > 640:
            ypos -= 50
            x = xpos
    floor(xpos,ypos)
    return

def floor(x_pos,y_pos):
    t.pu()
    t.setpos(x_pos,y_pos)
    t.pd()
    t.colormode(255)
    color = (209,209,224)
    t.fillcolor(color)
    t.begin_fill()
    rect(1280,600)
    t.end_fill()
    return

def rect(length,width):
    for x in range(2):
        t.fd(length)
        t.rt(90)
        t.fd(width)
        t.rt(90)
    return

def bars(x_pos,y_pos,color):
    t.pu()
    t.setpos(x_pos,y_pos)
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(2,540)
    t.fd(100)
    t.circle(2,540)
    t.fd(100)
    t.end_fill()

def right_cube(x_pos,y_pos,length,color):
    t.pu()
    t.setpos(x_pos,y_pos)
    square(length,color)
    t.fillcolor(color)
    t.pd()
    t.begin_fill()
    t.fd(length)
    t.lt(135)
    t.fd(50)
    t.lt(45)
    t.fd(length)
    t.lt(135)
    t.fd(50)
    t.rt(180)
    t.fd(50)
    t.lt(135)
    t.fd(length)
    t.lt(45)
    t.fd(50)
    t.lt(45)
    t.end_fill()
    return

def left_cube(x_pos,y_pos,length,color):
    t.pu()
    t.setpos(x_pos,y_pos)
    square(length,color)
    t.fillcolor(color)
    t.pd()
    t.begin_fill()
    t.lt(45)
    t.fd(50)
    t.rt(45)
    t.fd(length)
    t.rt(135)
    t.fd(50)
    t.rt(180)
    t.fd(50)
    t.rt(135)
    t.fd(length)
    t.rt(45)
    t.fd(50)
    t.rt(135)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.rt(180)
    t.end_fill()
    return


#<<<Color set up for some objects>>>#

t.colormode(255)
back_wall_color = (0,0,153)
windowFrame_color = (51,26,0)
wall_color = (133,133,173)
bar_color = (204,204,0)
cube_color = (179,0,134)
    
#<<<Start of Actual Drawing Program>>>#
t.speed(0)
background(-640,538,wall_color)
window(150,-500,450)
window(150,200,450)
bars(-100,350,bar_color)
bars(100,350,bar_color)
right_cube(450,100,60,cube_color)
left_cube(-600,-200,60,cube_color)
backBallPit(600,100,back_wall_color)
bottomBallPit(815,865,75,"blue")
leftBallPit(500,75,"blue")
rightBallPit(500,75,"blue")
ball(1500)