from graphics import*
import math
import random
import time

win = GraphWin('Sierpinski Trinagle',600,600)
win.setCoords(0,0,10,10)
win.setBackground('Black')

txt = Text(Point(9,9.5),'himanshup')
txt.setTextColor('White')
txt.draw(win)

a = 8
vertex = [Point(1,2), Point(a+1,2), Point(a/2+1,(3*a**2/4)**0.5+2)]
tri = Polygon(vertex[0], vertex[1], vertex[2])
tri.setOutline('white')
tri.draw(win)

#time.sleep(3)
p = Point(3,3)
p.setOutline('white')

for i in range(20000):
    
    p.setOutline('white')
    p.draw(win)

    rnd = random.choice(vertex)
    p = Point((p.getX()+rnd.getX())/2,(p.getY()+rnd.getY())/2)
  


