# day 17 exexercise 1
print("\nday 17 exexercise 1")
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print(nordic_countries)
print(es)
print(ru)



try:
    name = input("Your name: ")
    print(name + 2)
except Exception as e:
    print(e)
else:
    print("If right")
finally:
    print("Always")


lst = [2, 7]
numbers = range(2,7)
print(numbers)
numbers2 = range(*lst)
print(numbers2)

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = list(range(*args))  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]


def sum_all(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(sum_all(1,3,4,56,9,0))


def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))


for index, item in enumerate(["name",'age','city']):
    print(index, item)


fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f,v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, "vevegetable": v})
print(fruits_and_veges)
