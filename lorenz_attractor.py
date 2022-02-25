from vpython import*
import math
import time
import numpy as np

win = canvas(height=800, width=800)
win.camera.pos = vector(0,0,90)
win.camera.axis = vector(0,0,-90)
#label(pos=vector(8,10,0), text='himanshup', border='None',height=20)

rot = sphere(pos=vector(0,0,90), radius=0.002, opacity=0)

sig = 10
rho = 28
beta = 8/3

n = 25
dots = []

for i in range(n):
    c = vector(np.random.uniform(0,1),np.random.uniform(0,1),np.random.uniform(0,1))
    p = vector(np.random.uniform(-20,20),np.random.uniform(-20,20),np.random.uniform(-10,10))
    dots.append(sphere(pos=p, radius=0.2,color=c, make_trail=True, trail_radius=0.05, retain=10))

th = 0
cnt = 0
dt = 0.001
time.sleep(5)
while True:

    for dot in dots:
        old = dot.pos
        dot.pos += vector(sig*(old.y-old.x)*dt,(old.x*(rho-old.z)-old.y)*dt,(old.x*old.y-beta*old.z)*dt)
        if i == 1000:
            dot.retain = 300

    if i > 4000:
        rot.rotate(angle=dt, origin=vector(0,0,0), axis=vector(1,0.5,0))
        win.camera.pos = rot.pos
        rot.pos -= rot.pos*dt/10
        win.camera.axis = -win.camera.pos
        th += dt/2


    i += 1
    rate(80)
