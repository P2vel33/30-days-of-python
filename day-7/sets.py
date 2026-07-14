# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# day 7 level 1 exexercise 1
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update({'Twitter',"LG","Samsung"})
print(it_companies)
it_companies.pop()
print(it_companies)
var_remove = set("remove")
var_discard = set("discard")
print(var_remove.difference(var_discard))

