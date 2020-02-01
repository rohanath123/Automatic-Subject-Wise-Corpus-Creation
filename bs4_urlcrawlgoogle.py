import bs4 as bs 
import urllib.request
import requests

keyword = "dynamic programming"
keyword = keyword.replace(" ", "+")
source = requests.get("https://www.google.dz/search?q=" + keyword)
soup = bs.BeautifulSoup(source.content)

links = soup.findAll("a")


for url in links:
	if "/url?q=" in str(url.get('href')):
		print(url.get('href'))





'''
import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.google.dz/search?q=see", 'html5lib')
soup = BeautifulSoup(page.content)
links = soup.findAll("a")

print(links[0])'''


