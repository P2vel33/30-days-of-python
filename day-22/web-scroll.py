import json
import requests
from bs4 import BeautifulSoup

url = "https://www.bu.edu/president/boston-university-facts-stats/"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content,"html.parser")
print(soup.get_text())
# a = {: up.get_text()}

# with f as open("path", "a"):
    # f.
breakpoint()