# Author: Darsh Jhunjhunwal
# Date: 06-08-2023
# Bio: I'm 7 years old. I like to do programming

# import turtle
# for x in range(0, 3):
#     print("hello %d" % x)

# for x in range(1,11):
#     print("19x%d="%x)
#     print(19*x)

# for x in range(1,11):
#     print("19x%d=%d"%(x,19*x))

# for y in range(1,21):
#     print("\nTable of %d"%y)
#     for x in range(1,11):
#         print("%dx%d=%d"%(y,x,y*x))
    

# for x in range(0,5):
#     answer=input("10*5=?\n")
#     num = int(answer)
#     if num==50:
#         print("Very good")
#     else:
#         print("You need to learn multiplication")
# d = turtle.Pen()
# d.shape('turtle')

# for x in range(0, 4):
#     d.forward(100)
#     d.left(90)
# d.hideturtle()



# input("Press enter key to exit...")

friend_names = [
    'Akshaj', 'Priya','Chandan', 'Shree', 'Aayush'
      ]           
friend_age = [
    7, 10, 37, 7, 7
               ]
for x in friend_names:
    print("%s is one of my friends"% x)

for x in range(0,5):
     print("%s is one of my friends"%friend_names[x])
     print("%s will be %s years old after fifteen years\n"% (friend_names[x],friend_age[x]+15))




for y in range(1,21):
    print("\nTable of %d"%y)
    # print("%dx1=%d"%(y,y*1))
    # print("%dx2=%d"%(y,y*2))
    # print("%dx3=%d"%(y,y*3))
    # print("%dx4=%d"%(y,y*4))
    # print("%dx5=%d"%(y,y*5))
    # print("%dx6=%d"%(y,y*6))
    # print("%dx7=%d"%(y,y*7))
    # print("%dx8=%d"%(y,y*8))
    # print("%dx9=%d"%(y,y*9))
    # print("%dx10=%d"%(y,y*10))
    for x in range(1,11):
       print("%dx%d=%d"%(y,x,y*x))
    # for x in range(1,11):
    #     print("%dx%d=%d"%(y,x,y*x))

