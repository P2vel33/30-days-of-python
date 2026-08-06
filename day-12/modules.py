import statistics
import sys
from string import ascii_letters, digits, ascii_uppercase
import random
array = [1,2,3,4,5,6,7]
print(statistics.mode(array))
print(sys.argv[0])
letters_digits = ascii_letters + digits
length = len(letters_digits)
hex_letter_numbers = digits + ascii_uppercase[:6]
length_hex_letter_numbers = len(hex_letter_numbers)

# day 12 level 1 exexercise 1
print("day 12 level 1 exexercise 1")
def random_user_id():
    result = ''
    for step in range(6):
        result += letters_digits[random.randint(0, length)]
    return result
print(random_user_id())

# day 12 level 1 exexercise 2
print("\nday 12 level 1 exexercise 2")
def user_id_gen_by_user():
    result = []
    count = int(input("Count: "))
    symbols = int(input("Symbols: "))
    for _ in range(count):
        code = ''
        for __ in range(symbols):
            code += letters_digits[random.randint(0, length)]
        result.append(code)
    return result
print(user_id_gen_by_user())

# day 12 level 1 exexercise 3
print("\nday 12 level 1 exexercise 3")
def rgb_color_gen():
    return 'rgb({},{},{})'.format(random.randint(0,255),random.randint(0,255),random.randint(0,255))
print(rgb_color_gen())

def hexa_color_gen():
    code = '#'
    for _ in range(6):
        code += hex_letter_numbers[int(random.random() * length_hex_letter_numbers)]
    return code
print(hexa_color_gen())



# day 12 level 2 exexercise 1
print("\nday 12 level 2 exexercise 1")
def list_of_hexa_colors():
    count = int(random.random() * 100)
    result = []
    for _ in range(count):
        result.append(hexa_color_gen())
    return result
print(list_of_hexa_colors())

# day 12 level 2 exexercise 2
print("\nday 12 level 2 exexercise 2")
def list_of_rgb_colors():
    count = int(random.random() * 100)
    result = []
    for _ in range(count):
        result.append(rgb_color_gen())
    return result
print(list_of_rgb_colors())

# day 12 level 2 exexercise 3
print("\nday 12 level 2 exexercise 3")
def generate_colors(type_response, count):
    result = []
    if type_response == 'hexa':
        for _ in range(count):
            result.append(hexa_color_gen())
        return result
    elif type_response == 'rgb':
        for _ in range(count):
            result.append(rgb_color_gen())
        return result
    else:
        return 'No available type!'
print(generate_colors('hexa',9))



# day 12 level 3 exexercise 1
print("\nday 12 level 3 exexercise 1")
def shuffle_list(entry_list):
    if type(entry_list) == list:
        result = []
        copy_entry_list = entry_list.copy()
        for _ in entry_list:
            print(_)
            random_num = random.randint(0, len(copy_entry_list) - 1)
            result.append(copy_entry_list.pop(random_num))
        return result
    else:
        return "The data entered is not a list!"
print(shuffle_list([1,2,3,4,5,6,7,8,9]))

# day 12 level 3 exexercise 2
print("\nday 12 level 3 exexercise 2")
def random_seven():
    set_result = set()
    while len(set_result) <= 7:
        set_result.add(random.randint(0, 9))
    return set_result
print(random_seven())


