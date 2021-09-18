from graphics import*
import math
import time
import random

win = GraphWin('Retrograde',600,600, autoflush=False)
win.setCoords(-10,-10,10,10)
win.setBackground('black')

txt = Text(Point(3,5.5),'himanshup')
txt.setTextColor('white')
txt.setSize(15)
txt.draw(win)

sun = Circle(Point(0,0), 0.6)
sun.setFill('yellow')
sun.draw(win)

orbit = Circle(Point(0,0),9)
orbit.setOutline('white')
orbit.draw(win)

mars = Circle(Point(-3,4),0.2)
mars.setFill('orange')
mars.draw(win)

earth = Circle(Point(3,0),0.3)
earth.setFill('blue')
earth.draw(win)

r = 1500/365
th = 0.01
cnt = 0

projection =[Point(11,11)]
image =[Point(11,11)]
win.update()
time.sleep(5)
while cnt < math.pi/2:

    pt1 = earth.getCenter()
    x1 = pt1.getX()*math.cos(th*r) - pt1.getY()*math.sin(th*r)
    y1 = pt1.getX()*math.sin(th*r) + pt1.getY()*math.cos(th*r)
    earth.move(x1 - pt1.getX(), y1 - pt1.getY())

    pt2 = mars.getCenter()
    x2 = pt2.getX()*math.cos(th) - pt2.getY()*math.sin(th)
    y2 = pt2.getX()*math.sin(th) + pt2.getY()*math.cos(th)
    mars.move(x2 - pt2.getX() , y2 - pt2.getY())

    m = (pt1.getY()-pt2.getY())/(pt1.getX()-pt2.getX())
    x = pt1.getX()
    y = pt1.getY()

    x1 = (m**2*x-m*y-(81+81*m**2-m**2*x**2+2*m*x*y-y**2)**0.5)/(1+m**2)
    y1 = -m*x+y+(m**3*x-m**2*y-m*(81+81*m**2-m**2*x**2+2*m*x*y-y**2)**0.5)/(1+m**2)
    cr = Circle(Point(x1,y1),0.1)
    cr.setFill('orange')
    image.append(cr)
    image[0].undraw()
    image.remove(image[0])
    image[-1].draw(win)

    ln = Line(Point(x1,y1),pt1)
    ln.setFill('white')
    projection.append(ln)
    projection[0].undraw()
    projection.remove(projection[0])
    projection[-1].draw(win)
    
    cnt += th
    update(20)

