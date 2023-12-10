acronyms = ["LOL", "IDK", "SMH", "TBH"]

print(acronyms[0])

#adding
acronyms1 = []

acronyms1.append('LOL')
acronyms1.append('TBH')
print(acronyms1[1])

#removing
acronyms2 = ["LOL", "IDK", "SMH", "TBH"]

acronyms2.remove("TBH")
del acronyms2[0]

print(acronyms2)

#check if

if 1 in [1,2,3,4,5]:
    print("True")

acronyms = ["LOL", "IDK", "SMH", "TBH"]
word = "BNF"

if word in acronyms:
    print(word + " is on the list")
else:
    print(word + " is not on the list")

#print list individualy

for acronym in acronyms:
    print(acronym)

# combining lists into one 

breakfast = ['Egg Sandwich', 'Bagel', 'Coffee']
lunch = ['BLT', 'PB&J', 'Turkey Sandwich']
dinner = ['Soup', 'Salad', 'Spaghetti', 'Taco']

menu = [['Egg Sandwich', 'Bagel', 'Coffee'],
        ['BLT', 'PB&J', 'Turkey Sandwich'],
        ['Soup', 'Salad', 'Spaghetti', 'Taco']]

print('Breakfast Menu:\t', menu[0])
print('Lunch Menu: \t', menu[1])
print('Dinner Menu: \t', menu[2])

print(menu[0][1])

#dictionary with a keys

menus = { 'Breakfast': ['Egg Sandwich', 'Bagel', 'Coffee'],
          'Lunch': ['BLT', 'PB&J', 'Turkey Sandwich'],
          'Dinner': ['Soup', 'Salad', 'Spaghetti', 'Taco']}

print('Breakfast Menu:\t', menus['Breakfast'])
print('Lunch Menu: \t', menus['Dinner'])
print('Dinner Menu: \t', menus['Lunch'])

for  name, menu in menus.items():
    print(name, ' :', menu)

#using dictionary to represent objects

person = {'name': 'Jakub Sosnowski',
          'city': 'Cracow',
          'age': 25}

print(person.get('name'), 'is', person.get('age'), 'years old')