# Author: Darsh Jhunjhunwal
# Date: 22-10-2023
# Bio: I'm 7 years old. I like to do programming

from cupcakes import per_day_income
cost_per_cupcake=25
total_income=0

made1=input("how many cupcakes were made on day1?\n")
spoilt1=input("how many cupcakes were spoilt on day 1?\n")

made1=int(made1)
spoilt1=int(spoilt1)

print("Day1:")
total_income = total_income + per_day_income(made1,spoilt1,cost_per_cupcake)





made2=input("how many cupcakes were made on day2?\n")
spoilt2=input("how many cupcakes were spoilt on day 2?\n")

made2=int(made2)
spoilt2=int(spoilt2)

print("Day2:")
total_income=total_income+per_day_income(made2,spoilt2,cost_per_cupcake)

print("Total_income=%s"%(total_income))






from cupcakes import per_day_income
cost_per_cupcake=25
total_income=0
for x in range (1,4):
    print("Day%s:"%(x))
    made=input("how many cupcakes were made ?\n")
    spoilt=input("how many cupcakes were spoilt  1?\n")

    made=int(made)
    spoilt=int(spoilt)
    total_income+=per_day_income(made2,spoilt2,cost_per_cupcake)
print("Total_income=%s"%(total_income))