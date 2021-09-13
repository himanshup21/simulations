from vpython import*
import math
import time

win = canvas(height=600, width=600)
win.camera.pos = vector(0,0,20)
win.camera.axis = vector(0,0,-20)
label(pos=vector(9,10,0), text='himanshup', border='None')

mirrors = []
rays = []
vel = [norm(vector(1,0.2,0))]*6

for i in range(6):
    for j in range(4):
        mirrors.append(cylinder(pos=vector(-5+3*j,7-3*i,0), radius = 1, axis=vector(0,0,0.2), opacity=0.9))


rays.append(sphere(pos=vector(-10,-2.00000002,0), radius = 0.01,color=color.red, make_trail=True, trail_radius=0.05))
rays.append(sphere(pos=vector(-10,-2.00000001,0), radius = 0.01,color=color.orange, make_trail=True, trail_radius=0.05))
rays.append(sphere(pos=vector(-10,-2,0), radius = 0.01,color=color.yellow, make_trail=True, trail_radius=0.05))
rays.append(sphere(pos=vector(-10,-1.99999999,0), radius = 0.01,color=color.green, make_trail=True, trail_radius=0.05))
rays.append(sphere(pos=vector(-10,-1.99999998,0), radius = 0.01,color=color.blue, make_trail=True, trail_radius=0.05))
rays.append(sphere(pos=vector(-10,-1.99999997,0), radius = 0.01,color=color.purple, make_trail=True, trail_radius=0.05))

dt = 0.05

#time.sleep(5)
while True:
    rate(80)
    
    for i in range(len(rays)):
        rays[i].pos += vel[i]*dt

        for j in range(len(mirrors)):
            if mag(mirrors[j].pos - rays[i].pos) <= 1 and  dot(mirrors[j].pos - rays[i].pos,vel[i])>0:
                vel[i] = vel[i] -2*proj(vel[i],norm(mirrors[j].pos - rays[i].pos))
        
