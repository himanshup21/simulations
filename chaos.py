from vpython import*
import math
import time

win = canvas(height=800, width=800)
win.camera.pos = vector(0,0,20)
win.camera.axis = vector(0,0,-20)
label(pos=vector(8,10,0), text='himanshup', border='None')


vessel = sphere(pos=vector(0,0,0), radius = 8, opacity = 0.1)
border = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=8.6, thickness=0.05, opacity=0.3)

ball = [sphere(pos=vector(0.0299,4,0), radius=0.4, color = color.red, make_trail=True, trail_type="points",
              interval=10, retain = 200, trail_radius = 0.05), sphere(pos=vector(0.03,4,0), radius=0.4, color = color.yellow, make_trail=True, trail_type="points",
              interval=10, retain = 200, trail_radius = 0.05)]

vel = [vector(0,0,0)]*2
g = vector(0,-9.8,0)
dt = 0.008
#time.sleep(3)
while True:
    rate(300)
    for i in range(2):
        vel[i] += g*dt
        ball[i].pos += vel[i]*dt

        if mag(ball[i].pos) >= 8 and dot(ball[i].pos,vel[i])>0:
            vel[i] = vel[i] -2*proj(vel[i],norm(ball[i].pos))

    
