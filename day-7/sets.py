# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# day 7 level 1 exexercise 1
print(len(it_companies))
# day 7 level 1 exexercise 2
it_companies.add('Twitter')
print(it_companies)
# day 7 level 1 exexercise 3
it_companies.update({'Twitter',"LG","Samsung"})
print(it_companies)
# day 7 level 1 exexercise 4
it_companies.pop()
print(it_companies)
# day 7 level 1 exexercise 5
var_remove = set("remove")
var_discard = set("discard")
print(var_remove.difference(var_discard))

# day 7 level 2 exexercise 1
C = A.union(B)
print(C)

# day 7 level 2 exexercise 2
print(A.intersection(B))

# day 7 level 2 exexercise 3
print(A.issubset(B))

# day 7 level 2 exexercise 4
print(A.isdisjoint(B))

# day 7 level 2 exexercise 6
print(A.symmetric_difference(B))

# day 7 level 2 exexercise 7
del A
del B

# day 7 level 3 exexercise 1
age= "age"
age_set = set(age)
age_list = list(age)
if len(age_list) > len(age_set):
    print("age_list > age_set")
else:
    print("age_set > age_list")    

# day 7 level 3 exexercise 3
words = "I am a teacher and I love to inspire and teach people" 
words_set = set(words.split(" "))
print(len(words_set)) 