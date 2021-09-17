from __future__ import division
from vpython import*
import math
import time

win = canvas(height=800 , width=800)

#label(pos=vector(0,25,-20), text='himanshup', border='None')

G = 6.67*(10**-11)
R = 64*10**6
M = 6*(10**24)
m = M/20


earth = sphere(pos=vector(0,0,0),radius=R, texture=textures.earth)
moon = sphere(pos=vector(20*R,0,0),radius=R/3,texture='https://vignette.wikia.nocookie.net/future/images/e/e9/Moon_map_mercator.jpg')
rocket = sphere(pos=vector(0,earth.radius+R/100,0), radius = R/40, make_trail=True, trail_type='points')
earth.rotate(angle=-1.3 , axis=vector(0,1,0))
earth.rotate(angle=-0.9, axis=vector(1,0,0))

win.camera.pos = vector(0,rocket.pos.y,5*R)
win.camera.axis = vector(0,0,-50*R)
#win.camera.pos = vector(0,0,40*R)

vel = vector(3000,10,0)
dt = 0.5
cnt = 0
c = 0
d = 0

def thrust():
    global vel , cnt
    vel = 1.5*vel
    cnt += 1

def dthrust():
    global vel
    vel = 0.7*vel
    

def change():
    if rocket.color == vector(1,1,1):
        rocket.color=color.red
    else:
        rocket.color=color.white

    

canvas.bind(win,'click',change)
canvas.bind(win,'keydown',dthrust)

#time.sleep(50)
while True:
    
    rate(10**20)
    
    if cnt==0 and win.camera.pos.z < 8*R:
        win.camera.pos += vector(0,-R/500000,R/50000)

    if cnt==3 and win.camera.pos.z < 22*R:
        win.camera.pos += vector(R/16000,0,R/10000)

    if mag(rocket.pos-moon.pos) < 2*R :
        win.camera.pos = vector(moon.pos.x,moon.pos.y,3*R)
        
    if vel.x<0 and vel.y<10 and vel.y>9:
        if cnt ==0 : thrust()
        else : cnt = 2
    if vector(1,0,0).diff_angle(vel)<0.55 and vel.y>0 and vel.x>0 and rocket.pos.x<0:
        if cnt == 2:
            thrust()
        
        
    if mag(rocket.pos-moon.pos) > 2*R and c==0:
        g1 = G*M/(mag(rocket.pos))**2
    else :
        g1=0
        c = 1

    g2 = G*m/(mag(rocket.pos-moon.pos))**2
    if mag(rocket.pos) >= R and mag(rocket.pos-moon.pos) >= 21*R/60:
        rocket.pos += vel*dt
        vel -= g1*norm(rocket.pos)*dt - g2*norm(moon.pos-rocket.pos)*dt

    if rocket.pos.x > (moon.pos.x-R/5) and d==0:
        vel = (g2*mag(rocket.pos-moon.pos))**0.5*norm(vel)
        d = 1

    earth.rotate(angle=-10**-6 , axis=vector(0,-1,1))
    moon.rotate(angle=10**-7, axis=vector(0,0,1))


