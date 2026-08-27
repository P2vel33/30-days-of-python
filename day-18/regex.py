import re

# day 18 level 1 exexercise 1
print("\nday 18 level 1 exexercise 1")
regex = r"\w+"
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
set_words_paragraph = set(re.findall(regex, paragraph))
result = []
for word in set_words_paragraph:
    result.append(tuple([len(re.findall(word, paragraph)), word]))
print(result)

# day 18 level 1 exexercise 2
print("\nday 18 level 1 exexercise 2")
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
points.sort(key=lambda x:int(x))
sorted_points = list(map(lambda x:int(x),points))
distanse = abs(sorted_points[0]) + abs(sorted_points[-1])
print(sorted_points)
print(distanse)



# day 18 level 2 exexercise 1
print("\nday 18 level 2 exexercise 1")
def is_valid_variable(var):
    regex = r"^[a-zA-Z_]\w*"
    match = re.fullmatch(regex,var)
    if match == None:
        return False
    return True
print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True
print(is_valid_variable('firstname1')) # True



# day 18 level 3 exexercise 1
print("\nday 18 level 3 exexercise 1")
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(text):
    regex = r'[^\s\w]*'
    return re.sub(regex, '', text)
cleaned_text= clean_text(sentence)
print(cleaned_text);

def most_frequent_words(text):
    result = []
    text_set = set(text.split(' '))
    for item_text in text_set:
        regex = r"\b" + re.escape(item_text) + r'\b'
        result.append(tuple([len(re.findall(regex, text)), item_text]))
    result.sort(key=lambda x:x[0], reverse=True)
    return result[0:3]



print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]