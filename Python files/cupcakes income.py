# Author: Darsh Jhunjhunwal
# Date: 01-10-2023
# Bio: I'm 7 years old. I like to do programming

from cupcakes import per_day_income
cost_per_cupcake=25

made1=input("how many cupcakes were made on day1?")
made1=int(made1)
spoilt1=input("how many cupcakes were spoilt on day 1?")
spoilt1=int(spoilt1)
print("Day1:")
per_day_income(made1,spoilt1,cost_per_cupcake)
made2=input("how many cupcakes were made on day2?")
made2=int(made2)
spoilt2=input("how many cupcakes were spoilt on day 2?")
spoilt2=int(spoilt2)
print("Day2:")
per_day_income(made2,spoilt2,cost_per_cupcake)
