# exexercise 6.1 level 1
tuple611 = tuple()
tuple612 = ()
print(tuple611,tuple612)

# exexercise 6.2 level 1
sisters = ("Smith", "Aaron")
brothers = ("Stark", "Bolton")
print(sisters, brothers)

# exexercise 6.3 level 1
brothers_and_sisters = brothers + sisters
print(brothers_and_sisters)

# exexercise 6.4 level 1
print(len(brothers_and_sisters))

# exexercise 6.5 level 1
parents = ('Targarian','Barateon')
family = brothers_and_sisters + parents
print(family)



# exexercise 6.1 level 2
parents6121 = family[-2:]
print(parents6121)

# exexercise 6.2 level 2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ("Beef","Milk","Fish")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# exexercise 6.3 level 2
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# exexercise 6.4 level 2
print(food_stuff_tp[len(food_stuff_tp) // 2])

# exexercise 6.5 level 2
print(food_stuff_lt[3:-3])

# exexercise 6.6 level 2
del food_stuff_tp

# exexercise 6.7 level 2
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Iceland" in nordic_countries)
print("Norway" in nordic_countries)