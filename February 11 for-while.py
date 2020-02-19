# Author: Adam Steinbach
# Day: 4
# Date: Feb. 11 2020
# Class: Basic if statement

#for loop
#print all letters except 'i' 'c' and 's'
'''
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter == "i" or letter == "c" or letter == "s":
        continue
    print('current letter is:', letter)
'''

#while loop
#set count = 0 - this is the precondition for our while
count = 1

while(count<400):
    count = count * 4
    if(count==1):
        print("run", count, "time")
    else:
        print("run", count, "times")
print(count)