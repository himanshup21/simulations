import turtle as t
import time
import random

win = t.Screen()
win.setup(height=800,width=800)
win.bgcolor('black')
win.title('covid-19')
win.tracer(0)


for i in range(5):
    win.register_shape(str(i)+'.gif')
    
def border():
    t.penup()
    t.hideturtle()
    t.speed(0)
    t.color('yellow') ; t.pensize(4)
    t.goto(-350,-350)
    t.pendown()
    t.goto(-350,300) ; t.goto(350,300)
    t.goto(350,-350) ; t.goto(-350,-350)

border()

class Candidate(t.Turtle):
    
    def __init__(self,shp):
        t.Turtle.__init__(self)
        self.shape(shp)
        self.penup() 
        self.speed(0) ; self.speed = random.uniform(1,2)
        self.goto(random.randint(-300,300),random.randint(-300,300))
        self.setheading(random.uniform(10,350))

    def move(self):
        if (self.xcor() > 340 or self.xcor() < -340):
            self.setheading(180-self.heading())
        if (self.ycor() > 290 or self.ycor() < -340):
            self.setheading(360-self.heading())
            
        self.fd(self.speed)

death_count = 0
def collision(x,y):
    global infec_count
    x1 = x.speed
    h1 = x.heading()
    dist = (x.xcor()-y.xcor())**2 + (x.ycor()-y.ycor())**2
    if dist**0.5 < 15:
        x.speed = y.speed
        y.speed = x1
        x.setheading(y.heading())
        y.setheading(h1)

        if ((x.shape()=='3.gif' or x.shape()=='4.gif') and y.shape()=='2.gif'):
            if (random.randint(1,10)<=8):
                infect.append(y)
                y.shape('3.gif')
        if (x.shape()=='2.gif' and (y.shape() == '3.gif'or x.shape()=='4.gif')):
            if (random.randint(1,10)<=8):
                infect.append(y)
                x.shape('3.gif')

        if (x.shape()=='2.gif' and y.shape() == '1.gif'):
            if (random.randint(1,10)<=6):
                infect.append(y)
                x.shape('3.gif')
        if (x.shape()=='1.gif' and y.shape() == '2.gif'):
            if (random.randint(1,10)<=6):
                infect.append(y)
                y.shape('3.gif')

        if ((x.shape()=='3.gif' or x.shape()=='4.gif') and y.shape()=='0.gif'):
            if (random.randint(1,10)<=3):
                infect.append(y)
                y.shape('1.gif')
        if (x.shape()=='0.gif' and (y.shape() == '3.gif'or x.shape()=='4.gif')):
            if (random.randint(1,10)<=3):
                infect.append(y)
                x.shape('1.gif')
                
        if (x.shape()=='0.gif' and y.shape() == '1.gif'):
            if (random.randint(1,10)<=2):
                infect.append(y)
                x.shape('1.gif')
        if (x.shape()=='1.gif' and y.shape() == '0.gif'):
            if (random.randint(1,10)<=2):
                infect.append(y)
                y.shape('1.gif')
                
cnt1 = 0
def recovery():
    global cand,cnt1,death_count
    if cnt1 > 1:
        for c in cand:
            if (c.shape()=='3.gif' or c.shape()=='1.gif'):
                if random.randint(1,10)<=4:
                    if (c.shape()=='3.gif') : c.shape('2.gif')
                    else : c.shape('0.gif')
                if random.randint(1,10)<=1:
                    if (c.shape()=='3.gif') : c.shape('4.gif')
    cnt1 += 1
    win.ontimer(recovery,3000)

cnt2 = 0
vaccinated = 2
def severe_death():
    global cand,cnt2,death_count, vaccinated
    if cnt1 > 2:
        for c in cand:
            if random.randint(1,100)==1:
                if c.shape()=='3.gif':
                    vaccinated += 1
                    c.shape('1.gif')
                if c.shape()=='2.gif':
                    vaccinated += 1
                    c.shape('0.gif')
                    
            if c.shape()=='4.gif':
                if random.randint(1,10)<=4:
                    c.shape('2.gif')
                else :
                    death_count += 1
                    cand.remove(c)
    cnt2 += 1
    win.ontimer(severe_death,4000)

class Counts(t.Turtle):
    def __init__(self):
        t.Turtle.__init__(self)
        self.ht() ; self.penup()
        self.speed(0)
        
    def update_counts(self):
        global death_count,infect, vaccinated
        self.clear()
        self.goto(-350,320)
        self.color('white')
        self.write('INFECTED : {}%'.format(len(list(dict.fromkeys(infect)))*2),move=False,align='left',font=('Arial',15,'bold'))

        self.goto(350,320)
        self.color('white')
        self.write('DEATH : {}%'.format(death_count*2),move=False,align='right',font=('Arial',15,'bold'))

        self.goto(0,320)
        self.color('white')
        self.write('VACCINATED : {}%'.format(vaccinated*2),move=False,align='center',font=('Arial',15,'bold'))
                   
        win.ontimer(self.update_counts,500)

cand=[]
for i in range(2):
    cand.append(Candidate('0.gif'))
    cand.append(Candidate('3.gif'))
for i in range(46): cand.append(Candidate('2.gif'))

infect = [0,1]
cnt = Counts()
cnt.update_counts()
recovery()
severe_death()

while True:
    win.update()
    #if cnt1 == 1 : time.sleep(5)
    for can1 in range(len(cand)):
        cand[can1].move()

        for can2 in range(can1+1,len(cand)):
            collision(cand[can1],cand[can2])
    
