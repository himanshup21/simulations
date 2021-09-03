from graphics import*
import math


win = GraphWin('Golden Rotation',650,650, autoflush=False)
win.setCoords(-10,-10,10,10)
win.setBackground('white')

txt = Text(Point(8,8.5),'himanshup')
txt.setSize(15)
txt.draw(win)

th = 2*math.pi*(math.sqrt(5)-1)/2
cr = []

for i in range(1,1000):
    circle = cr.append(Circle(Point(math.sqrt(i/15)*math.sin(th*i),math.sqrt(i/15)*math.cos(th*i)),(0.01*i**0.38 + 0.03)))#/10000+0.06)))         

for i in range(len(cr)):
    if i < 200 : cr[i].setFill('skyblue')
    elif i < 400 : cr[i].setFill('green')
    elif i < 600 : cr[i].setFill('yellow')
    elif i < 800 : cr[i].setFill('orange')
    else : cr[i].setFill('red')
    cr[i].draw(win)

while True:

    for i in range(len(cr)):
        pt = cr[i].getCenter()
        x = pt.getX()*math.cos(th) - pt.getY()*math.sin(th)
        y = pt.getX()*math.sin(th) + pt.getY()*math.cos(th)
        cr[i].move(x - pt.getX(), y - pt.getY())

    update(10)

    

