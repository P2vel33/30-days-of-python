import math

# day 11 level 1 exexercise 1
print("day 11 level 1 exexercise 1")
def add_two_numbers (a,b):
    return a + b
print(add_two_numbers(123,1524))

# day 11 level 1 exexercise 2
print("\nday 11 level 1 exexercise 2")
def calculate_area_circle (r):
    return math.pi * r ** 2
print(calculate_area_circle(8))

# day 11 level 1 exexercise 3
print("\nday 11 level 1 exexercise 3")
def add_all_nums (*args):
    result = 0;
    for arg in args:
        if type(arg) != int:
            return "Not all arguments are numbers!"
        else:
            result += arg
    return result
print(add_all_nums(8,2,5,7,21,9,4,436,2))

# day 11 level 1 exexercise 4
print("\nday 11 level 1 exexercise 4")
def convert_celsius_to_fahrenheit (temp):
    if type(temp) == int:
        return ( temp * 9 /5) + 32
    else:
        return "Argument aren`t number!"
print(convert_celsius_to_fahrenheit(8))

# day 11 level 1 exexercise 5
print("\nday 11 level 1 exexercise 5")
def check_season (month):
    month.strip()
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
check_season("June")
check_season("AAA")

# day 11 level 1 exexercise 6
print("\nday 11 level 1 exexercise 6")
def calculate_slope (x1,y1,x2,y2):
    print(type(x1), x1)
    if type(x1) != int or type(y1) != int or type(x2) != int or type(y2) != int:
        return "Not all arguments are numbers!"
    return (x2-x1)/(y2-y1)
print(calculate_slope(1,2,3,8))
position_1 = {"x1":1,"y1":2, "x2":3,"y2":8}
position_2 = {}
print(calculate_slope(*position_1))
