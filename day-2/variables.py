# exexercise 1
first_name, last_name, country, age, is_married = "Thomas", "Snow", "Spain", 24, False
full_name = first_name + ' ' + last_name
has_brother = input('Do you have brother?')
has_sister = input('Do you have sister?')

print("first_name:", first_name)
print("last_name:", last_name)
print("full_name:", full_name)
print("country:", country)
print("age:", age)
print("is_married:", is_married)
print("has_brother:", has_brother)
print("has_sister:", has_sister)

# exexercise 2
# exexercise 2.1
print("Type first_name", type(first_name))
print("Type last_name",type(last_name))
print("Type country",type(country))
print("Type age",type(age))
print("Type is_married",type(is_married))
print("Type full_name",type(full_name))
print("Type has_brother",type(has_brother))
print("Type has_sister",type(has_sister))

# exexercise 2.2
print("Length first_name:", len(first_name))

# exexercise 2.3
print(len(first_name) > len(last_name))

# exexercise 2.4
num_one = 5
num_two = 4

# exexercise 2.5
total = num_one + num_two 

# exexercise 2.6
diff = num_two - num_one 

# exexercise 2.7
multiplication = num_two * num_one 

# exexercise 2.8
division = num_one / num_two 

# exexercise 2.9
remainder = num_one % num_two 

# exexercise 2.10
exp = num_one ** num_two 

# exexercise 2.11
floor_division = num_one // num_two 

# exexercise 2.12
import math

r = 30
area_of_circle = math.pi * (r ** 2)
circum_of_circle = 4 * math.pi * r

print("area_of_circle: ",area_of_circle)
print("circum_of_circle: ",circum_of_circle)

# exexercise 2.12
first_name_input = input("Your name: ")
print("User first_name_input: ", first_name_input)
last_name_input = input("Your lastname: ")
print("User last_name_input: ", last_name_input)
age_input = input("Your age: ")
print("User age_input: ", age_input)

help('keywords')
