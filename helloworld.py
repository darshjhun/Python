print("Hello Darsh")

print("8-4 = ", 8-4)
print(8 - 4)

print("Number of seconds in a year = ", 365 * 24 * 60 * 60)

print(500 / 20)

print(5 + 30 * 20)

print((5 + 30) * 20)

print(((5 + 30) * 20) / 10)

print(5 + 30 * 20 / 10)

mango_price = 900
mango_weight = 10
total = mango_price * mango_weight

print("Total=", total)
# print("hello comment")
apple_price = mango_price - 20
apple_weight = 10

print("Total Apple cost:", apple_price*apple_weight)


number_of_days_in_year = 365
number_of_hour_in_a_day = 24
number_of_minutes_in_an_hour = 60
number_of_seconds_in_a_minute = 60

total_number_of_seconds_in_a_year = number_of_days_in_year * \
    number_of_hour_in_a_day*number_of_minutes_in_an_hour*number_of_seconds_in_a_minute
print("Total number of seconds in a year=", total_number_of_seconds_in_a_year)

pocket_money_per_day = 200
daily_expense = 100
saving_per_day = pocket_money_per_day-daily_expense
saving_in_a_year = saving_per_day*365
print("saving per day = ", saving_per_day)
print("Saving in a year = ", saving_in_a_year)

the_tkt = 1500
dsc = 100
print("tkt cost per year", the_tkt - dsc)

print("darsh_has_10kg_apples")
print("3kg_apples_were_rotten")
print("but_he_lived_alone_so_he_decided_to_more_5kg"
      "-so_total_he_returned_8kg")
print("10-8")

print(10-3-4+4+8-2+2-4)

print(10-3-4+4+8-2+2-4)

print('hi')


1/14736

cupcakes_made = 520
cupcakes_spoilt = 12
cost_of_each_cupcake = 25
mon_earned_on_day1 = (cupcakes_made-cupcakes_spoilt)*cost_of_each_cupcake
print(mon_earned_on_day1)

cupcakes_made = 100
cupcakes_spoilt = 0
cost_of_each_cupcake = 25
mon_earned_on_day2 = (cupcakes_made-cupcakes_spoilt)*cost_of_each_cupcake
print(mon_earned_on_day2)

cupcakes_made = 130
cupcakes_spoilt = 5
cost_of_each_cupcake = 25
mon_earned_on_day3 = (cupcakes_made-cupcakes_spoilt)*cost_of_each_cupcake
print(mon_earned_on_day3)

# My name is Darsh

print("783-567=", 783-567)

first_name = 'Darsh'
last_name = 'Jhunjhunwal'
print("Welcome", first_name, last_name)

first_name = "Darsh"
surname = "Jhunjhunwal"
age = 7
string_text = "%s %s is %s years old\n"
print(string_text % (first_name, surname, age))

string_text = first_name, surname, age
print(string_text)

print('%s %s is %s years old\n' % (first_name, surname, age))


first_name = "Darsh"
surname = "Jhunjhunwal"
age = 7
# My name is Darsh Jhunjhunwal and I'm 7 years old.
darsh = first_name, surname, age
print('My name is %s %s and I\'m %s years old\n' % (darsh))
print('My name is %s %s and I\'m %s years old\n' % (first_name, surname, age))

print("5*3", 5*3)
print("2*2", 2*2)
print("15+4", 15+4)
print("Total hours in a week", 5*3 + 2*2, "hours")

weekday_work = 5*4
weekend_work = 2*2
total_work = weekday_work + weekend_work
print("Total work per week is %s" % total_work)


def add(num1, num2, num3):
    print(num1+num2+num3)


add(100, 200, 300)


def multiply(a, s, d):
    print(a*s*d)


multiply(20, 30, 40)

# 2*3=6
# 2*30=60
# 20*3=60
# 20*30=600
# 20*30*1=600
# 20*30*10=6000


friend_names = ['Akshaj sinha', 'Priya jhunjhunwal',
                'Chandan jhunjhunwal', 'Shree', 'Aayush']
friend_age = [7, 10, 37, 7, 7]
print(friend_names)
print(friend_names[3])
print("In 13 years ,%s will be %s years old" %
      (friend_names[0], friend_age[0]+13))

friend_names[3] = 'Aarav'
friend_age[3] = 6
print(friend_names, friend_age, '\n')

friend_names[4] = 'Tanmay'
friend_age[4] = 8
print(friend_names, friend_age, '\n')

name_and_age = [friend_names, friend_age]
print(name_and_age[0])
print(name_and_age[1])

print(name_and_age[0][4])
print(name_and_age[1][4])


print(name_and_age, '\n')

nested_list = [[['hi']]]
print(nested_list[0][0][0])

nested_list1 = [1, [[['hi']]]]
print(nested_list1[1][0][0][0])

nested_list2 = [[1, 'Chandan'], [[[2, 'Priya']]], [[[3, 'Darsh', 4]]]]
print(nested_list2[2][0][0][1])

nested_list3 = [[[[[[[['My age is']]]]]]], [[[[[[[['7']]]]]]]]]
my_str = nested_list3[0][0][0][0][0][0][0][0]
age_str = nested_list3[1][0][0][0][0][0][0][0][0]
print("[%s %s]" % (my_str, age_str))

# ['My age is 7']
nested_list4 = [
    [
        [[[[[[[[[[[
            [[[[[[[[[[[[[7]]]]]]]]]]]]]
        ]]]]]]]]]]]
    ],
    [[[[[[[[[[[[[[[[[[[[[[[[[[['My age']]]]]]]]]]]]]]]]]]]]]]]]]]],
    [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[['is']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
]

my_str = 'My age'
my_is = 'is'
my_age = 7
print("['%s %s %s']" % (my_str, my_is, my_age))

print("['My age is 7']")

