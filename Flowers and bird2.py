import turtle
wn=turtle.Screen()
import time
wn.setup(1200,1100)
wn.bgcolor('pink')
wn.bgpic('grass.gif')
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
t6=turtle.Turtle()
t7=turtle.Turtle()

t1.up()
t2.up()
t3.up()
t4.up()
t5.up()
t6.up()
t7.up()

image1='flo1.gif'
image2='flo2.gif'
image3='flo3.gif'
image4='flo4.gif'
image5='flo5.gif'
image6='flo6.gif'
image=[]
for i in range (118):
    #print(i)
    i1=str(i)
    image.append(i1+'.gif')


wn.addshape(image1)
t1.shape(image1)
t1.goto(-100,-230)

wn.addshape(image2)
t2.shape(image2)
t2.goto(-300,-400)

wn.addshape(image3)
t3.shape(image3)
t3.goto(300,-170)

wn.addshape(image4)
t4.shape(image4)
t4.goto(0,235)

wn.addshape(image5)
t5.shape(image5)
t5.goto(-150,380)

wn.addshape(image6)
t6.shape(image6)
t6.goto(400,-350)

while True:
    
    for i in range (18):
        
        wn.addshape(image[i])
        t7.shape(image[i])
        time.sleep(0.1)

    def fly(x, y):
        t7.goto(x, y)
        
    wn.onclick(fly)







