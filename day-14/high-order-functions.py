countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
from string import ascii_uppercase 

# day 14 level 1 exexercise 3
print("\nday 14 level 1 exexercise 3")
from functools import reduce

# day 14 level 1 exexercise 4
print("\nday 14 level 1 exexercise 4")
for country in countries:
    print(country)

# day 14 level 1 exexercise 5
print("\nday 14 level 1 exexercise 5")
for name in names:
    print(name)

# day 14 level 1 exexercise 6
print("\nday 14 level 1 exexercise 6")
for number in numbers:
    print(number)



# day 14 level 2 exexercise 1
print("\nday 14 level 2 exexercise 1")
countries_map = list(map(lambda x: x.capitalize(), countries))
print("countries_map: ", countries_map)

# day 14 level 2 exexercise 2
print("\nday 14 level 2 exexercise 2")
numbers_map = list(map(lambda x: x ** 2, numbers))
print("numbers_map: ",numbers_map)

# day 14 level 2 exexercise 3
print("\nday 14 level 2 exexercise 3")
names_map = list(map(lambda name:name.capitalize(),names))
print("names_map: ", names_map)

# day 14 level 2 exexercise 4
print("\nday 14 level 2 exexercise 4")
def filter_countries(country):
    if "land" in country:
        return True
    return False
countries_filter_1 = list(filter(filter_countries,countries))
print("countries_filter: ",countries_filter_1)

# day 14 level 2 exexercise 5
print("\nday 14 level 2 exexercise 5")
def equal_six_country_length(country):
    if len(country) == 6:
        return True
    return False
countries_filter_2 = list(filter(equal_six_country_length,countries))
print("countries_filter_2: ",countries_filter_2)

# day 14 level 2 exexercise 6
print("\nday 14 level 2 exexercise 6")
def equal_or_more_six_country_length(country):
    if len(country) >= 6:
        return True
    return False
countries_filter_3 = list(filter(equal_or_more_six_country_length,countries))
print("countries_filter_3: ",countries_filter_3)

# day 14 level 2 exexercise 7
print("\nday 14 level 2 exexercise 7")
def start_with_E_country(country):
    if type(country) == str and country.startswith("E") :
        return True
    return False
countries_filter_4 = list(filter(start_with_E_country,countries))
print("countries_filter_4: ",countries_filter_4)

# day 14 level 2 exexercise 8
print("\nday 14 level 2 exexercise 8")
def add_nums(all, curr):
    print("all: ",all)
    print("curr: ",curr)
    return all + curr
arr = reduce(add_nums,list(map(lambda x: x** 2, list(filter(lambda x: x%2 == 0,numbers)))))
print("arr: ", arr)

# day 14 level 2 exexercise 9
print("\nday 14 level 2 exexercise 9")
def get_string_lists(ex_list):
    return list(filter(lambda x: type(x) == str, ex_list ))
print(get_string_lists(['1',2,True,"False","YES",""]))

# day 14 level 2 exexercise 10
print("\nday 14 level 2 exexercise 10")
numbers_reduce = reduce(add_nums, numbers)
print("numbers_reduce: ",numbers_reduce)

# day 14 level 2 exexercise 11
print("\nday 14 level 2 exexercise 11")
def add_country(all_countries, curr_country):
    return "{}, {}".format(all_countries,curr_country)
countries_reduce_1 = "{} are north European countries ".format(reduce(add_country,countries))
print(countries_reduce_1)

# day 14 level 2 exexercise 12
print("\nday 14 level 2 exexercise 12")
from pathlib import Path
import sys
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(project_root))
from data.coutries import countries as countries_from_data
def categorize_countries(mode):
    def categorize_country(country):
        if mode in country:
            return True
        else:
            return False
    return list(filter(categorize_country,countries_from_data))
print(categorize_countries('land'))
print(categorize_countries('ia'))
print(categorize_countries('island'))
print(categorize_countries('stan'))

# day 14 level 2 exexercise 13
print("\nday 14 level 2 exexercise 13")
def get_dictionary_countries():
    result = {}
    for symbol in ascii_uppercase:
        result[symbol] = 0
            
    def add_values_dictionary_countries(country):
        if result[country[0]]:
            result[country[0]] += 1
        else:
            result[country[0]] = 1
    for country in countries_from_data:
        add_values_dictionary_countries(country)
    return result
print(get_dictionary_countries())

# day 14 level 2 exexercise 14
print("\nday 14 level 2 exexercise 14")
def get_first_ten_countries():
    return countries_from_data[:10]
print(get_first_ten_countries())

# day 14 level 2 exexercise 15
print("\nday 14 level 2 exexercise 15")
def get_last_ten_countries():
    return countries_from_data[-10:]
print(get_last_ten_countries())