from __future__ import division
from vpython import*
import math
import time

win = canvas(height=500 , width=600)
win.camera.pos = vector(0,0,35)
win.camera.axis = vector(0,0,-5)
label(pos=vector(18,17,0), text='himanshup', border='None')
time.sleep(3)

hinge = sphere(pos=vector(8,15,0),radius=0.5, texture=textures.wood)
hinges = []
hinges.append(hinge)
for i in range(1,5):
    hinges.append(hinge.clone(pos=hinge.pos-i*vector(4,0,0)))

rope  = cylinder(pos=hinge.pos, radius=0.06, axis=vector(0,-20,0))
ropes = []
ropes.append(rope)
for i in range(1,5):
    ropes.append(rope.clone(pos=hinges[i].pos))
    
bob = sphere(pos=rope.pos-vector(0,20,0), radius=2)
bobs = []
bobs.append(bob)
for i in range(1,5):
    bobs.append(bob.clone(pos=ropes[i].pos-vector(0,20,0)))

rot = [pi/6,pi/6,0,0,-pi/6]
for i in range(5):
    bobs[i].rotate(rot[i], origin=hinges[i].pos, axis=vector(0,0,1))
    ropes[i].rotate(rot[i], origin=hinges[i].pos, axis=vector(0,0,1))

g = 9.8
theta = []
for i in range(5):
    theta.append(vector(0,-1,0).diff_angle(bobs[i].pos-ropes[i].pos))
w = [0,0,0,0,0]
dt = 0.001

while True:
    rate(1000)
    sign = []
    for i in range(5):
        if bobs[i].pos.x == hinges[i].pos.x : sign.append(1)
        else : sign.append((bobs[i].pos.x-hinges[i].pos.x)/abs(bobs[i].pos.x-hinges[i].pos.x))
    #print(sign)
    for i in range(4,-1,-1):
        w[i] -= g*sign[i]*sin(theta[i])*dt
        dtheta = w[i]*dt
        bobs[i].rotate(angle=dtheta, origin=hinges[i].pos, axis=vector(0,0,1))
        ropes[i].rotate(angle=dtheta, origin=hinges[i].pos, axis=vector(0,0,1))
        theta[i] = vector(0,-1,0).diff_angle(bobs[i].pos-ropes[i].pos)
    #print(theta)
    for i in range(5):
        for j in range(i,5):
            if abs(theta[i]-theta[j])<0.005 and theta[i]<0.001 and theta[j]<0.001:
                w[i],w[j] = w[j],w[i]
                

