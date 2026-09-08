import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np

from pathlib import Path
project_root = Path(__file__).parent.parent


# nums= [1,2,3,4,5]
# s = pd.Series(nums)
# print(s)

# nums_index = [1,2,3,4,5]
# s = pd.Series(nums_index, index=[1,2,3,4,5])
# print(s)

# fruits = ['Orange','Banana','Mango']
# fruits = pd.Series(fruits, index=[1, 2, 3])
# print(fruits)


# dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
# s = pd.Series(dct)
# print(s)

# s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
# print(s)



# data = [
#     ['Asabeneh', 'Finland', 'Helsink'],
#     ['David', 'UK', 'London'],
#     ['John', 'Sweden', 'Stockholm']
# ]
# dt = pd.DataFrame(data, columns=["Name","Country","City"])
# print(dt)

# data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
#     'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
# dt = pd.DataFrame(data)
# print(dt)

# data = [
#     {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
#     {'Name': 'David', 'Country': 'UK', 'City': 'London'},
#     {'Name': 'John', 'Country': 'Sweden', 'CityTwo': 'Stockholm'}]
# df = pd.DataFrame(data)
# print(df)


# df = pd.read_csv(f'{project_root}/data/weight-height.csv')
# print(df)
# print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method
# print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method
# print(df.shape) # as you can see 10000 rows and three columns
# print(df.columns)
# print(df["Height"].describe())


# data = [
#     {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
#     {"Name": "David", "Country":"UK","City":"London"},
#     {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
# df = pd.DataFrame(data)
# print(df)

# weights = [74, 78, 69]
# df['Weight'] = weights
# print(df)

# heights = [178,181,193]
# df['Height'] = heights
# print(df)

# df['Height'] = df['Height'] * 0.01
# print(df)

# def calculate_bmi():
#     weights = df['Weight']
#     heights = df['Height']
#     bmi = []
#     for w,h in zip(weights,heights):
#         b = w/(h*h)
#         bmi.append(b)
#     return bmi
# df["BMI"] = calculate_bmi()
# print(df)
# df['BMI'] = round(df['BMI'], 1)
# print(df)

# birth_year = pd.Series(['1769', '1985', '1990'], index=[2,0,1] )
# df["BY"] = birth_year
# print(df)
# current_year = pd.Series(2026, index=[0,1,2])
# df["CY"] = current_year
# print(df)
# print(df['Weight'].dtype)
# print(df['BY'].dtype)
# df['BY'] = df['BY'].astype(int)
# print(df['BY'].dtype)

# df['Age'] = df['CY']  - df['BY']
# print(df)
# print(df['Age'])
# print(df[df['Age'] > 120])



df = pd.read_csv(f'{project_root}/data/hacker_news.csv')
print(df)
print(df.head())
print(df.tail())
title_series = pd.Series(df['title'])
print(title_series)
print(type(title_series))
def has_python():
    title = df['title']
    result = []
    for item in title:
        if("python" in item):
            result.append(item)
    return result
print(has_python())

mask_python = df['title'].str.contains('python', case=False, na=False)
python_titles = df.loc[mask_python]
mask_js = df['title'].str.contains('JavaScript', case=False, na=False)
js_titles = df.loc[mask_js]
print(python_titles)
print(js_titles)
print(f'Rows: {df.shape[0]}, columns: {df.shape[1]}')
