# Author: Adam Steinbach
# Day: 4
# Date: Feb. 11 2020
# Class: Turtle basics

#clasic example spirograph
'''
from turtle import *
#import turtle
color('purple', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()
'''

#classic spiral helix pattern
import turtle
loadWindow = turtle.Screen()
turtle.speed(2)

for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick