# from pathlib import Path
# import sys

# project_root = Path(__file__).resolve().parent.parent
# sys.path.insert(0, str(project_root))
# # import webbrowser
# import requests
# import json


# from mypackage import arithmetic


# # url_lists = [
# #     'http://www.python.org',
# #     'https://www.linkedin.com/in/asabeneh/',
# #     'https://github.com/Asabeneh',
# #     'https://twitter.com/Asabeneh',
# # ]

# # for url in url_lists:
# #     webbrowser.open_new_tab(url)



# url = 'https://jsonplaceholder.typicode.com/posts'

# response = requests.get(url)
# print(response)
# print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
# # print(response.text) # gives all the text from the page
# posts = response.json()
# print(posts[:1])

# print(
#     arithmetic.remainder(50,3)

# )

import requests


url = 'http://www.gutenberg.org/files/1112/1112.txt'

response = requests.get(url)
response_json = response.json()
print(response_json)
