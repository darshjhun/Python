# Author: Darsh Jhunjhunwal
# Date: 22-10-2023
# Bio: I'm 7 years old. I like to do programming

class animals:
    
    class Cat:
        eyes = 2
        paws = 4
        body = "furry"
    
        def __init__(self, name_of_cat, hobby):
            self.name = name_of_cat
            self.hobby = hobby
    
        def walk(self):
            print("I'm walking")
    
        def catch_mouse(self):
            print("I caught a mouse")
    
        def speak(self):
            print("Hello! I am a cat and my name is %s and I have %s eyes, %s paws and love to catch mice" % (self.name, self.eyes, self.paws))
            print("I like to %s"%(self.hobby))

    # Create instances of the Cat class
    tom = Cat("Tom", "study")
    lovly = Cat("Lovly", "play")
    max = Cat("Max", "sleep")
    harsh = Cat("Harsh", "eat")
 
    # Access attributes and call methods
    print(lovly.eyes)
    print(tom.eyes)
    print(max.eyes)
    print(harsh.eyes)

    lovly.walk()
    tom.walk()
    max.walk()
    harsh.walk()

    lovly.catch_mouse()
    tom.catch_mouse()
    max.catch_mouse()
    harsh.catch_mouse()

    tom.speak()
    lovly.speak()
    max.speak()
    harsh.speak()

import turtle
darsh=turtle.Pen()
priya=turtle.Pen()
chandan=turtle.Pen()
priya.left(45)
chandan.right(90)
darsh.forward(100)
priya.forward(100)
chandan.forward(100)
darsh.reset()
priya.reset()
chandan.reset()
import turtle
t1=turtle.Pen()
t2=turtle.Pen()
t3=turtle.Pen()
t4=turtle.Pen()
t5=turtle.Pen()
t2.left(70)
t3.left(140)
t4.left(210)
t5.left(280)
t1.circle(50)
t2.circle(50)
t3.circle(50)
t4.circle(50)
t5.circle(50)
input("Press enter key to exit...")

class Bank:
    class account:
        def __init__(self, starting_amount, name):
            self.balance = starting_amount
            self.name = name
            self.print_balance()
        
        def deposit_money(self, amount):
            self.balance += amount
            print("$ %s deposit to %s's account" % (amount, self.name))
        
        def withdraw_money(self, amount):
            self.balance -= amount
            print("$ %s withdraw from %s's account" % (amount, self.name))
        
        def print_balance(self):
            print("Amount in %s's account: $%s" % (self.name, self.balance))

priya = Bank.account(2000, 'priya')
darsh = Bank.account(1500, 'darsh')
priya.withdraw_money(1000)
darsh.deposit_money(1000)
priya.print_balance()
darsh.print_balance()

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def find_perimeter(self):
        return 2 * (22/7) * self.radius
    
    def find_area(self):
        return (22/7) * self.radius**2

circ1 = Circle(20)
perimeter = circ1.find_perimeter()
area = circ1.find_area()

print(f"Perimeter of a Circle: {perimeter}")
print(f"Area of a Circle: {area}")
