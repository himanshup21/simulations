from vpython import*
import math
import time

win = canvas(height=600, width=600)
win.camera.pos = vector(0,0,20)
win.camera.axis = vector(0,0,-20)
label(pos=vector(7,9,0), text='himanshup', border='None')


hing = sphere(pos=vector(0,8,0), radius = 0.15)
bob =[sphere(pos=vector(0.001,2,0), radius = 0.4, make_trail=True, trail_radius=0.05, retain=25)]
spring =[helix(pos=hing.pos, axis=vector(bob[0].pos-hing.pos), radius = 0.2, coils = 9, thickness=0.1)]

g = vector(0,-9.8,0)
l = 6
m = 1
k = -2*m*g.y/l#m*(g.y/4-2*g.y)/l
vel = [vector(0,0,0)]

dt = 0.005

#time.sleep(5)
while True:
    rate(60)

    for i in range(len(bob)):
        vel[i] += (m*g + k*(mag(hing.pos-bob[i].pos)-l)*norm(hing.pos-bob[i].pos))/m
        bob[i].pos += vel[i]*dt
        spring[i].axis = bob[i].pos-hing.pos
