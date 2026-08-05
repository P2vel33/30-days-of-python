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

# day 11 level 1 exexercise 7
print("\nday 11 level 1 exexercise 7")
def solve_quadratic_eqn (a,b,c):
    discriminant = b**2 - 4 * a * c
    if discriminant >= 0:
        sqrt_discriminant = math.sqrt(discriminant)
        return ([(-b + sqrt_discriminant)/2 * a, (-b - sqrt_discriminant)/2 * a])
    else:
        return "There is no solution!"
print(solve_quadratic_eqn(3,-12,9))

# day 11 level 1 exexercise 8
print("\nday 11 level 1 exexercise 8")
def print_list (example_list):
    if (type(example_list)) == list:
        for item_of_list in example_list:
            print(item_of_list)
    else:
        return print("The data entered is not a list!")
print_list(['s',1,False])
print_list("sadw")

# day 11 level 1 exexercise 9
print("\nday 11 level 1 exexercise 9")
def reverse_list (example_list):
    if (type(example_list)) == list:
        result = []
        for item_of_list in example_list:
            result.insert(0,item_of_list)
        return result
    else:
        return "The data entered is not a list!"
print(reverse_list([1,2,3,4]))

# day 11 level 1 exexercise 10
print("\nday 11 level 1 exexercise 10")
def capitalize_list_items (example_list):
    if (type(example_list)) == list:
        result = []
        for item_of_list in example_list:
            if(type(item_of_list) == str):
                item_of_list = item_of_list.capitalize()
                result.insert(0,item_of_list)
            else:
                return "Not all list inputs are strings!"
        return result
    else:
        return print("The data entered is not a list!")
print(capitalize_list_items(['all','python']))

# day 11 level 1 exexercise 11
print("\nday 11 level 1 exexercise 11")
def add_item (example_list, new_item):
    if (type(example_list)) == list:
        example_list.append(new_item)
        return example_list
    else:
        return print("The data entered is not a list!")
print(add_item(['All', 'likes'],'python'))

# day 11 level 1 exexercise 12
print("\nday 11 level 1 exexercise 12")
def remove_item (example_list, rm_item):
    if (type(example_list)) == list:
        if(rm_item in example_list):
            example_list.remove(rm_item)
            return example_list
        else:
            return "This value is not in the list!"
    else:
        return "The data entered is not a list!"
print(remove_item(['All', 'likes', 'python'],'python'))

# day 11 level 1 exexercise 13
print("\nday 11 level 1 exexercise 13")
def sum_of_numbers (number):
    if type(number) == int:
        result = 0
        for i in range(number):
            result += i
        return result + number
    else:
        return "The input value is not a number"
print(sum_of_numbers(3))

# day 11 level 2 exexercise 1
print("\nday 11 level 2 exexercise 1")
def evens_and_odds (number):
    if type(number) == int and number > 0:
        result_odd = 0
        result_evens = 0
        for i in range(number+1):
            if(i % 2 == 0):
                result_odd += 1
            else:
                result_evens += 1
        return "The number of odds are {}. The number of evens are {}.".format(result_odd, result_evens) 
    else:
        return "The input value is not a number"
print(evens_and_odds(3))

# day 11 level 2 exexercise 2
print("\nday 11 level 2 exexercise 2")
def factorial (number):
    if type(number) == int and number > 0:
        result = 1
        for i in range(1,number+1):
            result *= i
        return result
    else:
        return "The input value is not a number"
print(factorial(4))

# day 11 level 2 exexercise 3
print("\nday 11 level 2 exexercise 3")
def is_empty (param):
    if param:
        return False
    else:
        return True
print(is_empty(4))

# day 11 level 2 exexercise 4
print("\nday 11 level 2 exexercise 4")
# calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std
def calculate_mean (entry_list):
    if type(entry_list) == list:
        sum_entry_list = 0
        for item_entry_list in entry_list:
            sum_entry_list += item_entry_list
        return sum_entry_list/len(entry_list)
    else:
        return "The data entered is not a list!"
print(calculate_mean([1,2,3,4,5,6,7]))

print("\n")
def calculate_median(entry_list):
    if type(entry_list) == list:
        entry_list.sort()
        return entry_list[len(entry_list)//2]
    else:
        return "The data entered is not a list!"
print(calculate_median([5,4,3,2,1,0]))

print("\n")
def calculate_mode(entry_list):
    if type(entry_list) == list:
        count_item_entry_list = {}
        for item_entry_list in entry_list:
            if item_entry_list in count_item_entry_list:
                count_item_entry_list[item_entry_list] += 1
            else:
                count_item_entry_list[item_entry_list] = 1
        return max(count_item_entry_list, key=count_item_entry_list.get)
    else:
        return "The data entered is not a list!"
print(calculate_mode([1,2,3,6,7,9,9,10,3,5,6,7,3,2,6,7,1,1,43,56,3,2,6,8,2]))

print("\n")
def calculate_range(entry_list):
    if type(entry_list) == list:

        return  min(entry_list), max(entry_list)
    else:
        return "The data entered is not a list!"
print(calculate_range([1,2,3,6,7,9,9,10,3,5,6,7,3,2,6,7,1,1,43,56,3,2,6,8,2]))


# day 11 level 2 exexercise 5
print("\nday 11 level 2 exexercise 5")
def greet(name):
    if name:
        return "Hello, {}!".format(name)
    else:
        return "Hello, Guest!"
print(greet("Roman"))

# day 11 level 2 exexercise 6
print("\nday 11 level 2 exexercise 6")
def show_args(**args):
    if args:
        result = {}
        for arg in args:
            result[arg] = args[arg]
        return result
    else:
        return "No input data!"
print(show_args(name="Alice", age=30, city="New York"))

# day 11 level 3 exexercise 1
print("\nday 11 level 3 exexercise 1")
def is_prime(num):
    if type(num) == int:
        if num == 2:
            return True
        num_sqrt = int(math.sqrt(num))
        for i in range(2,num_sqrt + 1):
            if num % i == 0:
                return False
        return True
    else:
        return "Data input isn`t a number!"
print(is_prime(4))

# day 11 level 3 exexercise 2
print("\nday 11 level 3 exexercise 2")
def item_unique(entry_list):
    if type(entry_list) == list:
        set_entry_list = set(entry_list)
        return len(set_entry_list) == len(entry_list)
    else:
        return "The data entered is not a list!"
print(item_unique([1,2,3,4,4]))

# day 11 level 3 exexercise 3
print("\nday 11 level 3 exexercise 3")
def type_item_unique(entry_list):
    if type(entry_list) == list:
        type_unique = type(entry_list[0])
        for item_entry_list in entry_list:
            if type(item_entry_list) != type_unique:
                return False
        return True
    else:
        return "The data entered is not a list!"
print(type_item_unique([1,2,3,4,4,"1"]))

# day 11 level 3 exexercise 5
print("\nday 11 level 3 exexercise 5")

from data.countries_data import countries_data
def most_spoken_languages(entry_list):
    if type(entry_list) == list:
        languages = {}
        for item_entry_list in entry_list:
            if item_entry_list['languages'] and type(item_entry_list['languages']) == list:
                for language in item_entry_list['languages']:
                    languages[language] = languages.get(language, 0) + 1
        return sorted(languages.items(), key=lambda x:x[1], reverse=True)[:20]
    else:
        return "The data entered is not a list!"
print(most_spoken_languages(countries_data))
def most_populated_countries(entry_list):
    if type(entry_list) == list:
        result = []
        for country_data in sorted(entry_list, key=lambda x:x["population"], reverse=True)[:20]:
            result.append({"country_name": country_data["name"], "country_population": country_data["population"]})
        return result

    else:
        return "The data entered is not a list!"
print(most_populated_countries(countries_data))




    
