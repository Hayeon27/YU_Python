'''
Project : Lab 2.5 (별 그리기)
Author : Len_somwhere
Last Updated Date : June 18 2022
'''
import turtle                             #import turtle module for drawing a star

turtle.setup(500, 500)                    #set width and height of canvas
t = turtle.Turtle()                       #make a new turtle instance as "t"
t.shape('turtle')                         #set the shape of a turtle as "turtle"
t.pencolor('red')                         #
t.width(10)                               #set the turtle's trail width at "10"

length = 200                              #length : 
cx, cy = 0, 0                             #cx, cy : # center position      
sx = cx - length / 2                      #sx : 
sy = cy + length / 6                      #sy :  이 부분은 좀 더 정확한 계산을 할 것
t.penup(); t.goto((sx, sy)); t.pendown()  #(1)

count = 0                                 #count : 
turn_angle = 360 * 2 / 5                  #turn_angle : 
while count < 5:                          #(while loop) - 
    t.forward(length)                     #
    t.right(turn_angle)                   #
    count += 1                            #

t.penup(); t.goto(0, 0); t.pendown()      #(2)

'''
(1) : 
(2) : 
'''