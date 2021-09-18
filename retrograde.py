from graphics import*
import math
import time

win = GraphWin('Retrograde',600,600, autoflush=False)
win.setCoords(-10.2,-10.2,10.2,10.2)
win.setBackground('black')


txt = Text(Point(8,8.5),'himanshup')
txt.setTextColor('white')
txt.setSize(15)
txt.draw(win)

sun = Circle(Point(0,0), 0.6)
sun.setFill('yellow')
sun.draw(win)

mars = Circle(Point(-5,0),0.2)
mars.setFill('black')
mars.draw(win)

fmars = Circle(Point(-5,0),0.2)
fmars.setFill('orange')
fmars.draw(win)

earth = Circle(Point(-3,0),0.3)
earth.setFill('black')
earth.draw(win)

fearth = Circle(Point(-3,0),0.3)
fearth.setFill('blue')
fearth.draw(win)


r = 687/365
th = 0.01
cnt  = 0
cnt1 = 0
trails = []
win.update()
time.sleep(5)
while True:
    
    if cnt < 2*math.pi:
        pt1 = earth.getCenter()
        x1 = pt1.getX()*math.cos(th*r) - pt1.getY()*math.sin(th*r)
        y1 = pt1.getX()*math.sin(th*r) + pt1.getY()*math.cos(th*r)
        earth.move(x1 - pt1.getX(), y1 - pt1.getY())
        fearth.move(x1 - pt1.getX(), y1 - pt1.getY())

        pt2 = mars.getCenter()
        x2 = pt2.getX()*math.cos(th) - pt2.getY()*math.sin(th)
        y2 = pt2.getX()*math.sin(th) + pt2.getY()*math.cos(th)
        mars.move(x2 - pt2.getX() , y2 - pt2.getY())
        fmars.move(x2 - pt2.getX() , y2 - pt2.getY())

    else:
        if cnt1 == 0 : time.sleep(1)
        mars.undraw()
        earth.undraw()
        pt1 = earth.getCenter()
        x1 = pt1.getX()*math.cos(th*r) - pt1.getY()*math.sin(th*r)
        y1 = pt1.getX()*math.sin(th*r) + pt1.getY()*math.cos(th*r)
        earth.move(x1 - pt1.getX(), y1 - pt1.getY())

        pt2 = mars.getCenter()
        x2 = pt2.getX()*math.cos(th) - pt2.getY()*math.sin(th)
        y2 = pt2.getX()*math.sin(th) + pt2.getY()*math.cos(th)
        mars.move(x2 - pt2.getX(), y2 - pt2.getY())
        fmars.move(x2 - x1 - pt2.getX() + pt1.getX(), y2 - y1 - pt2.getY() + pt1.getY())
         
        sun.move(pt1.getX()-x1,pt1.getY()-y1)
        
        trail = fmars.getCenter()
        trails.append(trail)
        if len(trails) > 200 :
            trails[0].undraw()
            trails.remove(trails[0])
        trail.setFill('orange')
        trail.draw(win)
        cnt1 = 1

    cnt += th
    update(100)
    

