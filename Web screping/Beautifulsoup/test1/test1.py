import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')


allLaptopTag = soup.find_all('div', {'class': 'card product-wrapper thumbnail'})

allProducts = []

for tag in allLaptopTag:
  productData = {}
  targetTag = tag.find('img', {'class':'img-fluid card-img-top image img-responsive'})
  if targetTag: 
    productData['img'] = 'https://webscraper.io'+targetTag.attrs['src']
  targetTag = tag.find('a', {'class': 'title'})
  if targetTag:
    productData['title'] = targetTag.string
    
  targetTag = tag.find('h4', {'class', 'float-end price card-title pull-right'})
  if targetTag:
    productData['price'] = float(targetTag.string.split('$')[1])
    
  targetTag = tag.find('p', {'class', 'description card-text'})
  if targetTag:
    productData['description'] = targetTag.string
  
  targetTag = tag.find('p', {'class': 'float-end review-count'})
  if targetTag:
    productData['rating'] = int(targetTag.string.split(' ')[0])
  
  targetTag = tag.select('.ratings p')[1]
  if targetTag:
    productData['stars'] = float(targetTag['data-rating'])
  
  allProducts.append(productData)


allProducts = json.dumps(allProducts, indent=2)


with open('test.json', 'w') as file:
  file.write(allProducts)
