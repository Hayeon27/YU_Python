'''
Project : Lab 2.3 (직사각형 그리기)
Author : Len_somwhere
Last Updated Date : June 18 2022
'''
import turtle                                          #import turtle module for drawing a rectangle

turtle.title("Drawing a rectangle")                    #set turtle's title as "Drawing a rectangle"
turtle.setup(300, 250)                                 #set width and height of canvas

t = turtle.Turtle()                                    #make a new turtle instance as "t"
t.shape("turtle")                                      #set the shape of a turtle as "turtle"
t.color("red")                                         #set the turtle's trail color to "red"
t.width(3)                                             #set the turtle's trail width at "3"

width, length = 200, 150                               #width, length : the rectangle's width and length
print("Drawing a rectangle(width = {}, length = {})"\
    .format(width, length))                            #print "width, length"

turn_angle = 90                                        #turn_angle : the angle of rotation of a turtle
t.home(); t.write(t.position())                        #write its position (the center point)
start_x, start_y = -width // 2, -length // 2           #start_x, start_y : start points which turtle will draw
t.up(); t.goto((start_x, start_y)); t.down()           #(1)
t.write(t.position())                                  #write its position (the starting point)

t.forward(width); t.left(turn_angle)                   #(2)
t.forward(length); t.left(turn_angle)
t.forward(width); t.left(turn_angle)
t.forward(length); t.left(turn_angle)

t.up(); t.home(); t.down()                             #(3)
input("press any key to exit")

'''
(1) : turtle goes to start point (start_x, start_y)  
(2) : turtle draws rectangle (width : "width", length : "length")
(3) : turtle goes home (0, 0)
'''