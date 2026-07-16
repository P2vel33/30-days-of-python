# day 8 exexercise 1
dog = {}
print(dog)

# day 8 exexercise 2
dog["name"] = "Rex"
dog["color"] = "Brown"
dog["color"] = "Breed"
dog["len_legs"] = 50
dog["age"] = 2
print(dog)

# day 8 exexercise 3
students = {"name": "Petir", "lastname": "Beilish", "age": 40,"gender": "male","country": "Vesteros","skill":["communication", "joker"]}
print(students)

# day 8 exexercise 4
print(len(students))

# day 8 exexercise 5
print(students["skill"])
print(type(students["skill"]))

# day 8 exexercise 6
students["skill"].append("management")
print(students["skill"])

# day 8 exexercise 7
print(students.keys())

# day 8 exexercise 8
print(students.values())

# day 8 exexercise 9
print(students.items())

# day 8 exexercise 10
students.pop("country")
print(students)

# day 8 exexercise 9
del students

