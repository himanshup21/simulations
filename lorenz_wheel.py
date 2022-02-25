from vpython import*
import math
import time
import numpy as np

win = canvas(height=800, width=800, background=color.white)
win.camera.pos = vector(0,0,20)
win.camera.axis = vector(0,0,-20)
label(pos=vector(8,10,0), text='himanshup', border='None',height=20)

n = 35
r = 8
buckets = []
water = []
rods = []
omega = vector(0,0,0)

for th in np.linspace(0.05,2*np.pi+0.05,n):
    buckets.append(cylinder(pos=vector(r*np.sin(th),r*np.cos(th),0), axis=vector(0,1,0), radius=0.5, opacity=0.2))
    water.append(cylinder(pos=vector(r*np.sin(th),r*np.cos(th),0), axis=vector(0,0,0), radius=0.5, color=color.blue))
    rods.append(cylinder(pos=vector(0,0,0), axis=vector(r*np.sin(th),r*np.cos(th),0), radius=0.04,opacity=0.1))

com = sphere(pos=vector(0,0,0),radius=0.1,color=color.red,make_trail=True,trail_radius=0.02)

fill = 0.7
drain = 0.1
dt = 0.01
M = 0.5
g = vector(0,-10,0)
desity = 20
friction = 7000
#time.sleep(5)
while True:

    mass = 0
    ps = vector(0,0,0)
    acc = vector(0,0,0)
    for i in range(len(buckets)):
            
        if buckets[i].pos.x>-1 and buckets[i].pos.x<1 and buckets[i].pos.y>0 and water[i].axis.y<1:
            water[i].axis.y += fill*dt
        if water[i].axis.y > 0.05:  
            water[i].axis.y -= drain*water[i].axis.y*dt
             
        acc += (cross(buckets[i].pos,(M+desity*water[i].axis.y)*g))
        mass += M+desity*water[i].axis.y
        ps += (M+desity*water[i].axis.y)*buckets[i].pos

    com.pos = ps/mass
    omega += ((acc-friction*omega)/(mass*r**2))*dt

    for i in range(len(buckets)):
        buckets[i].rotate(angle=(omega.z)*dt, origin = vector(0,0,0), axis=vector(0,0,1))
        buckets[i].axis = vector(0,1,0)
        water[i].pos = buckets[i].pos
        rods[i].axis = buckets[i].pos
            
            
    rate(500)
