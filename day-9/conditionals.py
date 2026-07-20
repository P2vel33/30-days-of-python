# day 9 level 1 exexercise 1
user_age = int(input("Your age: "))
print("You are old enough to learn to drive.") if user_age >= 18 else print("You need {} more years to learn to drive.".format(18-user_age))

# day 9 level 1 exexercise 2
developer_age = 24
if developer_age < user_age:
    print("You are {} {} older than me.".format(user_age -developer_age, 'year' if user_age - developer_age == 1 else 'years'))
else:
    print("You are {} {} younger than me.".format(developer_age-user_age, 'year' if developer_age-user_age == 1 else 'years'))
    
# day 9 level 1 exexercise 3
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print("{} is greater than {}".format(a,b))
elif a < b:
    print("{} is less than {}".format(a,b))
else:
    print("{} is equals than {}".format(a,b))
    
# day 9 level 2 exexercise 1
points = int(input("Your points: "))
if points >= 90:
    print("Your grade: A")
elif points >= 80:
    print("Your grade: B")
elif points >= 70:
    print("Your grade: C")
elif points >= 60:
    print("Your grade: D")
else:
    print("Your grade: F")
    
# day 9 level 2 exexercise 2
month = input("Month: ")
month = month.strip()
if month in ["September", "October","November"]:
    print("Autumn")
elif month in ["December", "January","February"]:
    print("Winter")
elif month in ["March", "April","May"]:
    print("Spring")
elif month in ["June", "July","August"]:
    print("Summer")
else:
    print("You entered a non-existent month")
    
    
# day 9 level 2 exexercise 3
fruits = ['banana', 'orange', 'mango', 'lemon']
new_friuts = input("Fruit: ")
if(new_friuts in fruits):
    print("That fruit already exist in the list")
else:
    fruits.append(new_friuts)
    print(fruits)
    
# day 9 level 3 exexercise 1
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if "skills" in person and type(person['skills'] == "list"):
    print(person['skills'][len(person["skills"]) // 2])
else:
    print("skills not found")

# day 9 level 3 exexercise 2
if "skills" in person:
    print("Python" in person['skills'])
else:
    print("skills not found")

# day 9 level 3 exexercise 3
if "skills" in person:
    if set(["React", "Node", "MongoDB"]).issubset(set(person["skills"])):
        print("He is a fullstack developer")
    elif set(["Node", "Python", "MongoDB"]).issubset(set(person["skills"])):
        print("He is a backend developer")
    elif set(['JavaScript', 'React']).issubset(set(person["skills"])):
        print("He is a frontend developer")
    else:
        print("He isn`t developer")
else:
    print("skills not found")

# day 9 level 3 exexercise 4
if person["is_married"] == True and person['country'] == 'Finland':
    print("{} {} lives in Finland. He is married.".format(person['first_name'],person['last_name']))

