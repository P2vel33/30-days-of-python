# day 13 exexercise 1
print("\nday 13 exexercise 1")
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_numbers = [number for number in numbers if number <= 0]
print(numbers,"->",filter_numbers)

# day 13 exexercise 2
print("\nday 13 exexercise 2")
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output_list_of_lists = [value for item_list in list_of_lists for value in item_list]
print(output_list_of_lists)

# day 13 exexercise 3
print("\nday 13 exexercise 3")
generation_list = [(i, 1, i, i**2,i**3,i**4, i**5) for i in range(0,11)]
print(generation_list)

# day 13 exexercise 4
print("\nday 13 exexercise 4")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output_contries = [[country[0].upper(),country[0].upper()[0:3],country[1].upper()] for array in countries for country in array ]
print(output_contries)

# day 13 exexercise 5
print("\nday 13 exexercise 5")
output_contries_dictionary = [{'country':data_country[0].upper(), 'city': data_country[1].upper()} for country in countries for data_country in country ]
print(output_contries_dictionary)

# day 13 exexercise 6
print("\nday 13 exexercise 6")
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output_names = ['{} {}'.format(name_data[0] , name_data[1]) for name in names for name_data in name]
print(output_names)

# day 13 exexercise 7
print("\nday 13 exexercise 7")
intersectoin_y = lambda k,m: -m/k
print(intersectoin_y(2,4))

