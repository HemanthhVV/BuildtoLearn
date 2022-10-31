from turtle import *
from random import randint
import random
def shape(l,s):
    for j in range(10):
        color1=['yellow','green','red','blue','orange','pink','violet','indigo']
        c=random.choice(color1)
        d=random.choice(color1)
        penup()
        x=randint(-200,200)
        y=randint(-200,200)
        goto(x,y)
        pendown()
        color(c,d)
        begin_fill()
        for i in range(s):
            forward(l)
            right(360/s)
        end_fill()
a=int(input("Enter the length: "))
b=int(input("Enter the sides: "))
shape(a,b)
