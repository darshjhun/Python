# Author: Darsh Jhunjhunwal
# Date: 06-08-2023
# Bio: I'm 7 years old. I like to do programming
import turtle
print('hello world')

friend_names = ['Akshaj', 'Jatin', 'Shree', 'Aarav', 'Kabeer']
print(friend_names)
print(friend_names[0])
friend_ages = [7, 7, 8, 7, 8]
print("In 15 years , %s will be %syears old" %
      (friend_names[0], friend_ages[0]+15))
friend_names[4] = 'Darsh'

print(friend_names)
print(friend_ages)
names_and_ages = [friend_names, friend_ages]
print(names_and_ages)
print(names_and_ages[0][0])
friend_names.append('priya')
friend_names.append('Chandan')
print(friend_names)
del friend_names[3]
del friend_names[2]
print(friend_names)
names_and_ages_map = {'Vida': 9,
                      'Aarav': 7,
                      'Shree': 8,
                      'Darsh': 11,
                      'Akshaj': 6}
print(names_and_ages_map['Akshaj'])


token_map = {
    1: 'Darsh',
    2: 'Chandan',
    3: 'Priya'
}

print(token_map[2])


t = turtle.Pen()
t.shape('turtle')
t.speed(0)
t.forward(50000)
t.backward(50000)
t.clear()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.hideturtle()

t.reset()


t.backward(100)
t.up()
t.left(90)
t.forward(50)
t.right(90)
t.down()
t.forward(100)
t.backward(20)
t.right(90)
t.forward(50)
t.right(90)
t.forward(20)
t.right(90)
t.forward(50)
t.left(90)
t.forward(20)
t.left(90)
t.forward(50)
t.right(90)
t.forward(20)
t.right(90)
t.forward(50)
t.hideturtle()
t.reset()


t.backward(100)
t.left(90)
t.up()
t.forward(30)
t.down()
t.right(90)
t.forward(100)
t.hideturtle()
t.reset()
t.circle(50)
t.hideturtle()
t.reset()
t.color('blue')
t.circle(50)
t.reset()

t.circle(50)
t.fillcolor('red')
t.begin_fill()
t.circle(50)
t.end_fill()
#input("Press enter key to exit...")

number1 = float(input("Give number 1: "))
number2 = float(input("Give number 2: "))
print("Sum of %f and %f = %f" % (number1, number2, number1+number2))

name = input("Give me your name:")
if name=="Darsh" :
    print("You are Handsome")
    print("You are smart")
    print("You are dynamic")
else:
    print("%s is such a fool!" % name)


