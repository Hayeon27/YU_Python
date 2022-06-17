'''
Project : Lab 2.1 (직각 삼각형의 면적 및 둘레 계산)
Author : Len_somwhere
Last Updated Date : June 18 2022
'''
import math                                             #import math module for using sqrt function

width = int(input("width of right triangle = "))        #width : Triangles's width (convert str to int type)
height = int(input("height of right triangle = "))      #height : Triangles's height (convert str to int type)
diagonal = math.sqrt(width * width + height * height)   #diagonal : Triangle's diagonal (Using Pythagorean theorem)

area = width * height / 2                               #area : Triangle's area (Using the area formula of a triangle)
perimeter = width + height + diagonal                   #perimeter : Triangle's perimeter (The sum of the sides of a triangle)

print("Right triangle of width ({}) and height({}) => diagonal({})".format(width, height, diagonal))  #(1)
print("  area({}), perimeter({})".format(area, perimeter))                                            #(2)

'''
(1) : print "width, height, diagonal" using Formatting String
(2) : print "area, perimeter" using Formatting String
'''