import sys
import re
import json
from pathlib import Path
from functools import reduce

project_root = Path(__file__).parent.parent
sys.path.insert(0,str(project_root))

# day 19 level 1 exexercise 1
print("\nday 19 level 1 exexercise 1")
def count_words_lines(path_file):
    with open(path_file) as f:
        text = f.read().splitlines()
        def count_words(line):
            regex = r'\b\w+\b'
            list_word_line = re.findall(regex,line)
            return len(list_word_line)
        list_words = list(map(count_words, text))
        words = reduce(lambda x,y: x+y, list_words)
        return f'File: {path_file}: {(f'Number of words: {words}',f'Number of lines: {len(text)}')}'
print(count_words_lines(f'{project_root}/data/obama_speech.txt'))
print(count_words_lines(f'{project_root}/data/michelle_obama_speech.txt'))
print(count_words_lines(f'{project_root}/data/donald_speech.txt'))
print(count_words_lines(f'{project_root}/data/melina_trump_speech.txt'))

# day 19 level 1 exexercise 2
print("\nday 19 level 1 exexercise 2")
def most_spoken_languages(filename, count):
    try:
        with open(filename) as file:
            text = json.load(file)
            count_lang = dict()
            for country in text:
                    for lang in country["languages"]:
                        if(count_lang.get(lang)):
                            count_lang[lang] += 1
                        else:
                            count_lang[lang] = 1
            result = list(map(lambda x: (count_lang[x],x),list(count_lang)))
            result.sort(key=lambda x: x[0], reverse=True)
            return result[:count]
    except:
        print("This file isn`t JSON!")
print(most_spoken_languages(f'{project_root}/data/countries_data.json',10))
print(most_spoken_languages(f'{project_root}/data/countries_data.json',3))

# day 19 level 1 exexercise 3
print("\nday 19 level 1 exexercise 3")
def most_populated_countries(filename, count):
    try:
        with open(filename) as file:
            text = json.load(file)
            result = list(map(lambda x: {'country': x["name"], 'population': x["population"]}, text))
            result.sort(key=lambda x: x["population"])
            return result[:count]
    except:
        print("This file isn`t JSON!")
print(most_populated_countries(f'{project_root}/data/countries_data.json',10))
print(most_populated_countries(f'{project_root}/data/countries_data.json',3))



# day 19 level 2 exexercise 1
print("\nday 19 level 2 exexercise 1")
# try:
with open(f'{project_root}/data/email_exchanges_big.txt') as file:
    text = file.read()
    regex = r"From\s\S+"
    result = set(list(map(lambda x: x[5:],re.findall(regex,text))))
    print(result)
# except:
    # print("This file isn`t JSON!")

# day 19 level 2 exexercise 2
print("\nday 19 level 2 exexercise 2")
def find_most_common_words(filename, count):
    try:
        with open(filename) as file:
            text = file.read()
            regex = r"\b\w+\b"
            words_text = re.findall(regex,text, re.IGNORECASE)
            dict_words_count = {}
            for word in words_text:
                if(dict_words_count.get(word)):
                    dict_words_count[word] += 1
                else:
                    dict_words_count[word] = 1
            result = list(map(lambda x: (dict_words_count[x],x), dict_words_count))
            result.sort(key=lambda x: x[0], reverse=True)
            return result[:count]
    except:
        print("Error")
print(find_most_common_words(f'{project_root}/data/donald_speech.txt',1))

# day 19 level 2 exexercise 3
print("\nday 19 level 2 exexercise 3")
print(find_most_common_words(f'{project_root}/data/obama_speech.txt',10))
print(find_most_common_words(f'{project_root}/data/michelle_obama_speech.txt',10))
print(find_most_common_words(f'{project_root}/data/donald_speech.txt',10))
print(find_most_common_words(f'{project_root}/data/melina_trump_speech.txt',10))





