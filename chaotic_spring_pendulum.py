from vpython import*
import math
import time

win = canvas(height=800, width=800)
win.camera.pos = vector(0,0,20)
win.camera.axis = vector(0,0,-20)
label(pos=vector(9,10,0), text='himanshup', border='None')


hing = sphere(pos=vector(0,3,0), radius = 0.05)
bob =[sphere(pos=vector(3,-5,0), radius = 0.2, color=color.cyan, make_trail=True, trail_radius=0.01), sphere(pos=vector(3.01,-5,0), radius = 0.2, color=color.yellow, make_trail=True, trail_radius=0.01)]
spring =[helix(pos=hing.pos, axis=vector(bob[0].pos-hing.pos), radius = 0.1, coils = 15, thickness=0.05, color=color.cyan), helix(pos=hing.pos, axis=vector(bob[1].pos-hing.pos), radius = 0.1, coils = 15, thickness=0.05, color=color.yellow)]

g = vector(0,-9.8,0)
k = 20
l = 2.9
m = 3
vel = [vector(0,0,0)]*2

dt = 0.001
#time.sleep(5)
while True:
    rate(50)

    for i in range(len(bob)):
        vel[i] += (m*g + k*(mag(hing.pos-bob[i].pos)-l)*norm(hing.pos-bob[i].pos))/m
        bob[i].pos += vel[i]*dt
        spring[i].axis = bob[i].pos-hing.pos
