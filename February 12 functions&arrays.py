# Author: Adam Steinbach
# Day: 5
# Date: Feb. 11 2020
# Class: functions and arrays

#a really really simple function
'''
def f(x):
    #a 1 line funtion
    return x **2+10

#out of function into main program
x=46
print("Results of my calculation are: ", f(x))
'''

#slightly more complex but still basic
'''
def song(day):
    if (day=="third"):
        print("three french hens,", song("second"), song("first"))
    if (day == "second"):
        print("two turtle doves, and", song("first"))
    if (day == "first"):
        print("a partridge in a pear tree. ")

#main program for running my function
#ask for input
num=input("Please enter a day in the form of first to twelth: ")
print("On the", num, "day of christmas, my true love gave to me ", song(num))
'''

#import array library
from array import*
'''
my_array = array('i', [1,2,3,4])
print(my_array)
'''

#slightly different
import array as arr

a=arr.array('d', [1, 3.5, 7.9])
print(a)
print("first element: ", a[0])
print("second element: ", a[1])
print("last element: ", a[-1])

#look up add slicing, AND changing values in an array