# Author: Adam Steinbach
# Day: 3
# Date: Feb. 10 2020
# Class: Basic if statement

#ex 1 if
'''
i = 20
if(i<15):
    print(i, "is smaller than 15")
    print("inside if")
'''

#ex 2 if else
'''
i = 20
if(i<15):
    print(i, "is smaller than 15")
    print("inside if")
else:
    print(i, "is greater than 15")
    print("outside if")
'''

#ex 3 nested ifs and elif
'''
i = 120
if(i<=10):
    print(i, "is less than or equal to 10")
    print("inside if")
elif(i<=15):
    print(i, "is less than or equal to 15")
    print("inside elif")
else:
    print(i, "is greater than 15")
    print("inside else")
print("outside if, elif, else")
'''

#ex 4 for loop, iterating over a list
print("My List")
l = ["apples", "blueberries", "canteloupe", "dragon fruit"]
for i in 1:
    print(i)