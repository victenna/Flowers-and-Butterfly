#file Flowers and butterfly(2)
import turtle
wn=turtle.Screen()
import time
wn.setup(900,700)
wn.bgcolor('pink')
wn.bgpic('grass.gif')
flowers=['flo0.gif','flo1.gif',\
         'flo2.gif','flo3.gif',\
        'flo4.gif','flo5.gif']
flower=[]
for n in range (6):
    wn.addshape(flowers[n])
    flower.append(turtle.Turtle(flowers[n]))
    flower[n].up()
    
    
flower[0].goto(-100,-230)
flower[1].goto(-300,-120)
flower[2].goto(300,-170)
flower[3].goto(0,235)
flower[4].goto(120,50)
flower[5].goto(-250,150)

butterfly=[]
for i in range (18):
    i1=str(i)
    butterfly.append(i1+'.gif')
t=turtle.Turtle()
t.up()


while True:
    for i in range (18):
        wn.addshape(butterfly[i])
        t.shape(butterfly[i])
        time.sleep(0.1)
    

    def fly(x, y):
        t.goto(x, y)
    wn.onclick(fly)







