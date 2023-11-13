MyList = ['Darsh', 'Chandan', 'Priya']
city = 'Pune'

MyDictionary = {'names': MyList, 'city': city}

print("My keys\n")
for key in MyDictionary.keys():
    print(key)

print("My values\n")
for value in MyDictionary.values():
    print(value)

print(MyDictionary['names'])
