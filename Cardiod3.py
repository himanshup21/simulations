from vpython import*
import math
import time

win = canvas(height=800, width=800)
win.camera.pos = vector(0,0,20)
win.camera.axis = vector(0,0,-20)
label(pos=vector(8,10,0), text='himanshup', border='None')
label(pos=vector(-10,5,0), text='Light', border='None',height = 20)
label(pos=vector(-10,4,0), text='Source', border='None',height = 20)

source = cylinder(pos=vector(-9,0,0), axis=vector(0,0,0.01), radius=0.4, color = color.orange)
border = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=9, thickness=0.1,)
pointer = arrow(pos=vector(-10,3,0), axis = vector(source.pos - vector(-10,3,0))*0.7, shaftwidth = 0.1, headwidth = 0.3, headlength = 0.4) 

n = 100
rays = []
vel = []
theta = pi/2.1
cnt = [0]*n

for i in range(n):
    rays.append(sphere(pos=vector(-9,0,0), radius=0.01, color = color.orange, make_trail=True, trail_radius = 0.02))
    vel.append(vector(cos(theta),sin(theta),0))
    theta -= 2*pi/(2.1*n)
    
dt = 0.1
time.sleep(5)
while True:
    rate(50)
    
    for i in range(len(rays)):
        rays[i].pos += vel[i]*dt
        
        if mag(rays[i].pos) >= 9 and dot(rays[i].pos,vel[i])>0:
            vel[i] = vel[i] -2*proj(vel[i],norm(rays[i].pos))
            cnt[i] += 1

        for j in range(len(rays)):
            if cnt[j] == 18:
                vel[i] = vector(0,0,0)
                

