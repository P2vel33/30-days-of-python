import math
# # exexercise 3.1
# developer_age:int = 24

# # exexercise 3.2
# developer_height:float = 1.78

# # exexercise 3.3
# complex_var:complex = 1.78 + 1j

# # exexercise 3.4
# triangle_base = input("3.4 Enter base: ")
# triangle_height = input("3.4 Enter height: ")
# area = float(triangle_base) * float(triangle_height) / 2
# print("The area of the triangle is " + str(area))

# # exexercise 3.5
# triangle_a = input("3.5 Enter triangle_a: ")
# triangle_b = input("3.5 Enter triangle_b: ")
# triangle_c = input("3.5 Enter triangle_c: ")
# perimeter  = float(triangle_a) + float(triangle_b) + float(triangle_c);
# print("The perimeter of the triangle is " + str(perimeter))

# # exexercise 3.6
# rectangle_height = input("3.6 Enter rectangle_height: ")
# rectangle_width = input("3.6 Enter rectangle_width: ")
# perimeter  = float(triangle_a) + float(triangle_b) + float(triangle_c);
# print("The perimeter of the triangle is " + str(perimeter))

# # exexercise 3.7
# radius = input("3.7 Enter radius: ")
# area_37  = float(radius) ** 2 * math.pi ;
# circumference_37 = 2 * math.pi * float(radius)
# print("The area_37 is " + str(area_37))
# print("The circumference_37 is " + str(circumference_37))

# exexercise 3.8
# x_38 = float(input("3.8 x = "))
# def y_38(x):
#     return 2 * x + 2
# y38_intercept = 2 * 0 + 2
# x38_intercept = -2 / 2
# slope38 = (0 - x_38) / (y_38(0) - y_38(x_38))
# print("The slope38 is " + str(slope38))
# print("The x38_intercept is " + str(x38_intercept))
# print("The y38_intercept is " + str(y38_intercept))

# # exexercise 3.9
# a39 = (2,2)
# b39 = (6,10)
# def m(a,b):
#     return (b[1] - a[1])/(b[0] - a[0])
# slope39 = m(a39,b39)
# def euclidean_distance(a,b):
#     return math.sqrt((a[0] - a[1])**2 + (b[0] - b[1])**2)
# print("The slope39 is " + str(slope39))
# print("The euclidean_distance is " + str(euclidean_distance(a39,b39)))

# # exexercise 3.10
# print(slope38 > slope39)

# # exexercise 3.11
# def y311(x):
#     return x**2 + 6*x + 9
# D = 6**2 - 4 * 1 * 9
# x_311_01 = (-6 + math.sqrt(D))/2
# x_311_02 = (-6 - math.sqrt(D))/2
# print(x_311_01,x_311_02)

# # exexercise 3.12
# print("Len python = " + str(len("python")))
# print("Len dragon = " + str(len("dragon")))
# print(len("python") == len("dragon"))

# exexercise 3.13
print("python and dragon have on: " + str("on" in "python" and "on" in "dragon"))

# exexercise 3.14
string314 = "I hope this course is not full of jargon"
print(string314 +" have jargon: " + str("jargon" in string314 ))

# exexercise 3.15
string315_1 = "python"
string315_2 = "dragon"
print(string315_1 +" and "+ string315_2 + " not have on: " + str(not "on" in "python" and "on" in "dragon"))

# exexercise 3.16
string315_1 = "python"
# string315_1 = float(string315_1)
string315_1 = str(string315_1)
print(len(string315_1))

# exexercise 3.17
num_317 = input("number = ")
num_317 = float(num_317)
print("Number is even:", num_317 % 2 == 0)

# exexercise 3.18
num_318_1 =7/3
num_318_2 =2.7
print(num_318_1 == num_318_2)

# exexercise 3.18
print(type('10') == type(10))

# exexercise 3.19
print(float('9.8') == 10)

# exexercise 3.20
hours320 = int(input("Enter hours: "))
rate_per_hour_320 = float(input("Enter rate per hour: "))
print("Your weekly earning is",hours320 * rate_per_hour_320)

# exexercise 3.21
years321 = int(input("Enter number of years you have lived: "))
print("You have lived for ",years321 * 365 * 24 * 60 * 60, "seconds.")

# exexercise 3.22
def func322(x):
    result = ''
    for i in range(4):
        result += str(x ** i)
        if i != 4:
            result += ' ' 
    return result
print(func322(1))
print(func322(2))
print(func322(3))
print(func322(4))
print(func322(5))



