from turtle import *
from random import randint
import random
def shape(l,s):
    color('red','light yellow')
    begin_fill()
    for j in range(4):
        forward(100)
        right(90)
    left(45)
    forward(70)
    right(90)
    forward(70)
    left(45)
    #triangleends
    forward(150)
    right(90)
    forward(100)
    right(90)
    forward(150)
    #rectangleends
    forward(40)
    right(90)
    forward(45)
    left(90)
    forward(20)
    left(90)
    forward(45)
    #doorends
    right(90)
    forward(40)
    right(90)
    forward(100)
    right(45)
    forward(70)
    right(45)
    forward(150)
    right(45)
    forward(70)
    end_fill()
shape(5,1)
'''a=int(input("Enter the length: "))
b=int(input("Enter the sides: "))
shape(a,b)'''
