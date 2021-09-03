from graphics import*
import math
import time

win = GraphWin('Earth-venus',650,650, autoflush=False)
win.setCoords(-10,-10,10,10)
win.setBackground('black')

txt = Text(Point(8,8.5),'himanshup')
txt.setTextColor('white')
txt.setSize(15)
txt.draw(win)

sun = Circle(Point(0,0), 1)
sun.setFill('yellow')
sun.draw(win)

venus = Circle(Point(-5,0),0.25)
venus.setFill('orange')
venus.draw(win)
v_orbit = Circle(Point(0,0),abs(venus.getCenter().getX()))
v_orbit.setOutline('orange')
v_orbit.setWidth(4)
v_orbit.draw(win)

earth = Circle(Point(-7,0),0.4)
earth.setFill('blue')
earth.draw(win)
e_orbit = Circle(Point(0,0),abs(earth.getCenter().getX()))
e_orbit.setOutline('blue')
e_orbit.setWidth(4)
e_orbit.draw(win)

r = 8/13
th = 0.1
cnt  = 1
win.update()
#time.sleep(5)
while cnt < int(25*math.pi/th):

    pt = venus.getCenter()
    x = pt.getX()*math.cos(th) - pt.getY()*math.sin(th)
    y = pt.getX()*math.sin(th) + pt.getY()*math.cos(th)
    venus.move(x - pt.getX(), y - pt.getY())

    pt1 = earth.getCenter()
    x = pt1.getX()*math.cos(th*r) - pt1.getY()*math.sin(th*r)
    y = pt1.getX()*math.sin(th*r) + pt1.getY()*math.cos(th*r)
    earth.move(x - pt1.getX(), y - pt1.getY())

    ln = Line(earth.getCenter(),venus.getCenter())
    ln.setOutline('white')
    ln.draw(win)

    if cnt%51 == 0:
        sun.undraw()
        v_orbit.undraw()
        sun.draw(win)
        v_orbit.draw(win)

    cnt += 1
    update(60)

time.sleep(1)

sun.undraw()
venus.undraw()
earth.undraw()
v_orbit.undraw()
e_orbit.undraw()


