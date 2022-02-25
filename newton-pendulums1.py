from __future__ import division
from vpython import*
import math
import time

win = canvas(height=500 , width=600)
win.camera.pos = vector(0,0,35)
win.camera.axis = vector(0,0,-5)
label(pos=vector(18,17,0), text='himanshup', border='None')

hinges = []
ropes = []
bobs = []

for i in range(5):
    hinges.append(sphere(pos=vector(8-4*i,15,0),radius=0.5, texture=textures.wood))
    ropes.append(cylinder(pos=hinges[-1].pos, radius=0.06, axis=vector(0,-20,0)))
    bobs.append(sphere(pos=ropes[-1].pos-vector(0,20,0), radius=2))

theta = [pi/6,pi/6,0,0,-pi/6]
omega = [vector(0,0,0)]*5
for i in range(5):
    bobs[i].rotate(theta[i], origin=hinges[i].pos, axis=vector(0,0,1))
    ropes[i].rotate(theta[i], origin=hinges[i].pos, axis=vector(0,0,1))

g = vector(0,-9.8,0)
m = 1
dt = 0.002
time.sleep(5)
while True:
    
    for i in range(5):
        acc = cross(bobs[i].pos-hinges[i].pos,m*g)/(m*mag(bobs[i].pos-hinges[i].pos)**2)
        omega[i] += acc*dt
        bobs[i].rotate(angle=omega[i].z*dt, origin=hinges[i].pos, axis=vector(0,0,1))
        ropes[i].rotate(angle=omega[i].z*dt, origin=hinges[i].pos, axis=vector(0,0,1))

        for j in range(i+1,5):
            if mag(bobs[i].pos-bobs[j].pos) < 4:# and omega[i].z*omega[j].z<=0:
                omega[i],omega[j] = omega[j],omega[i]
                

    rate(1000)
        
                

