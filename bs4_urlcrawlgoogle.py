import bs4 as bs 
import urllib.request
import requests

keyword = "asap rocky"
keyword = keyword.replace(" ", "+")
source = requests.get("https://www.google.dz/search?q=" + keyword)
soup = bs.BeautifulSoup(source.content)

links = soup.findAll("a")

urls = []
for url in links:
	if "/url?q=" in str(url.get('href')):
		urls.append(str(url.get('href')).strip("/url?q="))


print(urls)


