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