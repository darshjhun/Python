# Author: Darsh Jhunjhunwal
# Date: 06-08-2023
# Bio: I'm 7 years old. I like to do programming

# Write a program, Asking user "10x5=?"
# if user writes correct answer, print "Very good"
# Else print, "You need to learn multipltion"
answer=input("10*5=?\n")
if answer=="50":
    print("Very good")
else:
    print("You need to learn multiplication")

name=input("Give me your name ")

if name=="Darsh": 
    print("You are Handsome")
else:
    print("%s is such a fool"% name)



# write a program, where user gives an input color name
# if the color is red, then print "Stop! Danger ahead!"
# Else print "You may go!"

colour=input("what is the signal colour?\n")
if colour=='red':
    print("Stop! Danger ahead!")
else:
    print("You may go!")
    

# write a program, asking user to input a number below 10.
# If the number < 10, print "Very good!"
# else print, print "You need to learn numbers"

number=input("write a number below 10\n")
num=int(number)
if num < 10: 
    print("Very good!")
else:
    print("You need to learn numbers")  

