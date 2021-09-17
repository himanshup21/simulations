from vpython import*
import random
import math
import time
import pygame
from pygame import mixer

#root = Tk()
win = canvas(height=600, width=400)
win.camera.pos = vector(0,0,20)
win.camera.axis = vector(0,0,-20)

pygame.init()


ball = sphere(pos=vector(0,-14,0), radius=3, texture='https://media.istockphoto.com/vectors/football-soccer-background-vector-id857142754?k=6&m=857142754&s=612x612&w=0&h=iUZBeLXB5JRcUIJjDZslJqz2H_yogVWs0zs7s04NYGQ=')
ground = box(pos=vector(0,0,-10), size=vector(32,48,0.1), texture= 'black-brick-wall-free-photo.jpg')

vel=vector(0,0,0)
omega = vector(0,0,0)

def bounce():
    global vel,omega
    
    if ((ball.pos.x-win.mouse.pos.x)**2+(ball.pos.y-win.mouse.pos.y)**2) < 9:
        
        mixer.Sound('kick.wav').play()
        
        dy = random.uniform(0,abs(ball.pos.y-win.mouse.pos.y))

        if abs(win.mouse.pos.x - ball.pos.x) < 0.8 : dx=0
        else:
            if win.mouse.pos.x > ball.pos.x:
                dx = random.uniform(-dy,0)
            else : dx = random.uniform(0,dy)
            
        dirc = vector(dx,dy,0)
        vel = 18*norm(dirc)
        if dx!=0 : omega += cross((win.mouse.pos-ball.pos),dirc)*1/2
    

canvas.bind(win,'click',bounce)

dt = 0.01
g = vector(0,-10,0)

while True:
    rate(300)
    
    ball.pos += vel*dt
    vel += g*dt

    if ball.pos.y <= -14 and vel.y <0 :
        vel.y = -0.6*vel.y

        if abs(vel.y)>2: mixer.Sound('kick.wav').play()
        v = cross(vector(0,-1,0),omega)
        
        if v.x*vel.x >= 0:
            omega = (2*mag(omega)/7+5*abs(vel.x)/7)*norm(omega)
            vel.x = cross(vector(0,-1,0),omega).x
            
        elif mag(omega) > 5*abs(vel.x)/2:
            omega = ((2*mag(omega)-5*abs(vel.x))/7)*norm(omega)
            vel.x = cross(vector(0,-1,0),omega).x

        elif mag(omega) <= 5*abs(vel.x)/2:
            omega = ((2*mag(omega)-5*abs(vel.x))/7)*norm(omega)
            vel.x = cross(vector(0,-1,0),omega).x
        
                

    if (ball.pos.x <= -8.5 and vel.x < 0) or (ball.pos.x >= 8.5 and vel.x > 0):
        vel.x = -0.5*vel.x
        mixer.Sound('kick.wav').play()
        v = cross(vector(-1,0,0),omega)
        
        if v.y*vel.y >= 0:
            omega = (2*mag(omega)/7+5*abs(vel.y)/7)*norm(omega)
            vel.y = cross(vector(-1,0,0),omega).y

        elif mag(omega) > 5*abs(vel.y)/2:
            omega = ((2*mag(omega)-5*abs(vel.y))/7)*norm(omega)
            vel.y = cross(vector(-1,0,0),omega).y

        elif mag(omega) <= 5*abs(vel.y)/2:
            omega = ((2*mag(omega)-5*abs(vel.y))/7)*norm(omega)
            vel.y = cross(vector(-1,0,0),omega).y
    '''       
    if (abs(vel.x) < 0.5 and ball.pos.y<=-14) :
        vel = vector(0,0,0)
        omega = vector(0,0,0)
    '''
    ball.rotate(omega.z*dt,vector(0,0,1))
        
    

