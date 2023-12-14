import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')


allPhones = []

allPhonesTags = soup.find_all('div', {'class': 'card product-wrapper thumbnail'})


for phonetag in allPhonesTags:
  phonData = {}
  phonData['img'] = 'https://webscraper.io'+phonetag.find('img', {'class': 'img-fluid card-img-top image img-responsive'}).attrs['src']
  phonData['description'] = phonetag.find('p', {'class': 'description card-text'}).string
  phonData['title'] = phonetag.find('a', {'class': 'title'}).string
  reviewTag = phonetag.find('p', {'class': 'float-end review-count'})
  phonData['rating'] = float(reviewTag.find_next('p').attrs['data-rating'])
  try:
    phonData['reviews'] = int(reviewTag.string.split(' ')[0])
  except ValueError:
    pass
  try:
    phonData['price'] = float(phonetag.find('h4', {'class': 'float-end price card-title pull-right'}).string[1:])
  except ValueError :
    pass
    
  allPhones.append(phonData)
pprint(allPhones)