'''
Project : Homework 2.1 (원의 면적 및 둘레 계산)
Author : Len_somwhere
Last Updated Date : June 20 2022
'''
import math                     #import math module for using math.pi

rad = int(input("radius : "))   #rad : a value to be entered as radius

area = math.pi * rad * rad      #area : the area of a circle (using the formula for the area of a circle)
circum = 2 * math.pi * rad      #circum : the circumference of a circle (using the formula for the circumference of a circle)

print("Circle of radius ({}) : area ({}), circumference ({})"\
    .format(rad, area, circum)) #print "rad, area, circum"
