from vpython import*
import math
import time

win = canvas(height=800, width=800)
win.camera.pos = vector(0,0,20)
win.camera.axis = vector(0,0,-20)
label(pos=vector(8,10,0), text='himanshup', border='None')

coin1 = cylinder(pos=vector(0,0,0), axis=vector(0,0,0.4), radius = 2.5 , texture = 'c.png')
#coin1.visibile = False 
coin2 = cylinder(pos=vector(0,0,0) + + vector(2*coin1.radius,0,0), axis=vector(0,0,0.4), radius = 2.5 , texture = 'c.png' )
point = sphere(pos=coin1.pos + vector(coin1.radius,0,0.3), radius=0.2, color=color.orange, make_trail=True)
#line = cylinder(pos = vector(0,0,0), radius=0.2, axis = point.pos)

th = 0.01

time.sleep(5)
for i in range(943):
    rate(100)
    coin2.rotate(th, axis=vector(0,0,1), origin=coin1.pos)
    point.rotate(th, axis=vector(0,0,1), origin=coin1.pos)
    coin2.rotate(th, axis=vector(0,0,1), origin=coin2.pos)
    point.rotate(th, axis=vector(0,0,1), origin=coin2.pos)
    #line.axis = point.pos

