'''
Project : Lab 2.2 (입력데이터의 통계 분석)
Author : Len_somwhere
Last Updated Date : June 18 2022
'''
import math                           #import math module for using sqrt function

TARGET_NUM_DATA = 10                  #TARGET_NUM_DATA : target number of data to be input (Target : 10)
num_data = 0                          #num_data : variable for the number of data to be input (Initial value : 0)
L_data = []                           #L_data : list for storing "data" (Initial value : empty list)
L_sum = 0                             #L_sum : variable to contain the sum of "data" (Initial value : 0)

print("Input {} integer data."\
    .format(TARGET_NUM_DATA))         #print "TARGET_NUM_DATA" using Formatting String

while num_data < TARGET_NUM_DATA:     #(while loop) - to receive data
    data = int(input("data = "))      #data : variable to contain the value of the input string converted to int type
    num_data += 1                     #calculate increasing 1 on "num_data"
    L_data.append(data)               #add "data" as an element to the "L_data" list
    L_sum += data                     #calculate increasing "data" on "L_sum"

avg = L_sum / num_data                #avg : the result value obtained by dividing "L_sum" by "num_data"
diff_sq_sum = 0                       #diff_sq_sum : variable to contain the sum of the difference's squares

for i in range(num_data):             #(for loop) - to calculate difference and the sum of its squares
    diff = avg - L_data[i]            #diff : the result value obtained by subtracting "avg" by "the [i] index value of L_data" (difference)
    diff_sq_sum += diff * diff        #diff_sq_sum : the sum of differences' squares

var = diff_sq_sum / num_data          #var : the result value obtained by dividing "diff_sq_sum" by "num_data" (variance)
std = math.sqrt(var)                  #std : the result value of square root operation of "var" (standard deviation)

print("Input data list = ", L_data)   #print "L_data" using Formatting String
print("avg = {}, var = {}, std = {}"\
    .format(avg, var, std))           #print "avg, var, std" using Formatting String