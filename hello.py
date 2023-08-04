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

print(token_map[token_number])
