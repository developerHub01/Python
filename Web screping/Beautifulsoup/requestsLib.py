import requests

url = "https://www.wscubetech.com/training-courses.html"

r = requests.get(url)
print(r.text)