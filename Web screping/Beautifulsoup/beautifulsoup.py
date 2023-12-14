import requests
from bs4 import BeautifulSoup

url = "https://www.wscubetech.com/training-courses.html"

r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, "lxml")
print(soup)