import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

tag = soup.div.p
print(tag)
# to get inner text of a tag
print(tag.string)
print(soup.header.div.a.span.string)