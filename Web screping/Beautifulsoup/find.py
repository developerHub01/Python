import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/product/572"
url2 = "https://webscraper.io/test-sites/e-commerce/allinone"

r = requests.get(url)
r2 = requests.get(url2)

soup = BeautifulSoup(r.text, 'lxml')
soup2 = BeautifulSoup(r2.text, 'lxml')
# print(soup.find('h4', {"class": "float-end price pull-right"}))
# print(soup.find('h4', {"class": "float-end price pull-right"}).string)
# print(soup.findAll('h4', {"class": "float-end price pull-right"}))

print(soup2.findAll('h4', {'class': 'float-end price card-title pull-right'}))
prices = soup2.findAll('h4', {'class': 'float-end price card-title pull-right'})

for i, price in enumerate(prices):
  prices[i] = price.string[1:]
  
print(prices)
