'''
Project : Homework 2.2 (직사각형의 면적 및 둘레 계산)
Author : Len_somwhere
Last Updated Date : June 20 2022
'''
input_str = input("width, length : ")                 #input_str : a value to be entered as width and length

width, length = map(int, input_str.split(sep = ' '))  #(1)

area = width * length                                 #area : the area of a rectangle (using the formula of the area of a rectangle)
peri = 2 * (width + length)                           #peri : the perimeter of a rectangle (using the formula of the perimeter of a rectangle)

print("Rectangle of width ({}) and length ({}) : area ({}), perimeter ({})")\
    .format(width, length, area, peri)                #print "width, length, area, peri"

'''
(1) : separate words based on spaces, convert them to int format, and store them in width and length variables
 - width : the width of a rectangle
 - length : the length of a rectangle
'''