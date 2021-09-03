import turtle as t
import math
import time

win = t.Screen()
win.bgcolor('black')
win.setup(height=600 , width = 600)
#win.tracer(0)

t.shape('circle')
t.shapesize(0.1)
t.goto(-60,-20)
t.color('white')
t.ht()
t.speed(0)

i = 0

#time.sleep(10)
while True:
    t.stamp()
    t.fd(15)
    t.lt(math.pi/6+i)
    i += math.pi/3             #increment
    win.update()

