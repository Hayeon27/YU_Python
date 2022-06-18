'''
Project : Lab 2.4 (정삼각형 그리기)
Author : Len_somwhere
Last Updated Date : June 18 2022
'''
import math                                      #import math module for using tangent function
import turtle                                    #import turtle module for drawing a centered triangle

turtle.setup(400, 400)                           #set width and height of canvas
turtle.title("Drawing a centered triangle")      #set turtle's title as "Drawing a centered triangle"
t = turtle.Turtle()                              #make a new turtle instance as "t"
t.shape('turtle')                                #set the shape of a turtle as "turtle"
t.pencolor('blue')
t.width(10)                                      #set the turtle's trail width at "10"

side_length = 200                                #side_length : 
turn_angle = 360 / 3                             #turn_angle : 
h = side_length / (2.0 * math.tan(math.pi / 3))  #(1)
x0, y0 = -side_length / 2, -h                    #x0, y0 :      

print("x0, y0 = ", x0, y0)                       #
t.dot(5, "red")                                  #
t.write(t.pos())                                 #

t.up(); t.goto(x0, y0); t.down()                 #(2)
for i in range(3):                               #(for loop) - 
    t.write(t.pos())                             #
    t.forward(side_length)                       #
    t.left(turn_angle)                           #

t.up(); t.goto(0, 0); t.down()                   #(3)

'''
(1) : 
(2) : 
(3) : 
'''