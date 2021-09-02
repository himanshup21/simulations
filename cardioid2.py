from graphics import*
import math
import time

win = GraphWin('Cardioid',650,650, autoflush=False)
win.setCoords(-10,-10,10,10)
win.setBackground('black')

txt = Text(Point(7,7.5),'himanshup')
txt.setTextColor('white')
txt.setSize(10)
txt.draw(win)

circle = Circle(Point(0,0),4)
circle.setOutline('white')
circle.setWidth(4)
circle.draw(win)

center = Circle(Point(0,0),0.2)
center.setFill('white')
center.draw(win)

pt = [Point(0,4),Point(6,4),Point(-6,4)]
ln = [Line(Point(0,0),pt[0]),Line(pt[1],pt[2])]
lnn = Line(Point(4,0),Point(4,0))


th = 0.01
time.sleep(5)
for i in range(1100):
    
    x0 = pt[0].getX()*math.cos(th) - pt[0].getY()*math.sin(th)
    y0 = pt[0].getX()*math.sin(th) + pt[0].getY()*math.cos(th)
    x1 = pt[1].getX()*math.cos(th) - pt[1].getY()*math.sin(th)
    y1 = pt[1].getX()*math.sin(th) + pt[1].getY()*math.cos(th)
    x2 = pt[2].getX()*math.cos(th) - pt[2].getY()*math.sin(th)
    y2 = pt[2].getX()*math.sin(th) + pt[2].getY()*math.cos(th)
    
    pt = [Point(x0, y0), Point(x1, y1), Point(x2, y2)]

    ln[0].undraw()
    ln[0] = Line(Point(0,0),pt[0])
    ln[0].setWidth(2)
    ln[0].setOutline('white')
    ln[0].draw(win)

    ln[1].undraw()
    ln[1] = Line(pt[1],pt[2])
    ln[1].setWidth(2)
    ln[1].setOutline('white')
    ln[1].draw(win)

    lnn.undraw()
    m = (y2-y1)/(x2-x1)
    c = y0 - m*x0
    point = Point((4-m*c)/(1+m**2) , (4*m+c)/(1+m**2))
    #trace = Circle(point,0.1)
    point.setFill('orange')
    point.draw(win)
    lnn = Line(Point(4,0),point)
    lnn.setWidth(4)
    lnn.setOutline('orange')
    lnn.draw(win)

    if i%51 == 0:
        circle.undraw()
        circle.draw(win)

    update(100)
    
