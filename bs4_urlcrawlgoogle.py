import bs4 as bs 
import urllib.request
import requests
from pprint import pprint
keyword = "elon musk"
keyword = keyword.replace(" ", "+")
source = requests.get("https://www.google.dz/search?q=" + keyword)
soup = bs.BeautifulSoup(source.content, 'lxml')

links = soup.findAll("a")

urls = []
for url in links:
	if "/url?q=" in str(url.get('href')):
		urls.append(str(url.get('href')).strip("/url?q="))

urls_clean = [str(urls[i])[0:str(urls[i]).find("&sa")] for i in range(len(urls))]
urls_clean.pop(len(urls_clean)-1)

source2 = urllib.request.urlopen(urls_clean[12]).read()
soup = bs.BeautifulSoup(source2, 'lxml')

content = []
for url in urls_clean:
	try:
		source2 = urllib.request.urlopen(url).read()
		soup = bs.BeautifulSoup(source2, 'lxml')
		for paragraph in soup.find_all('p'):
			content.append(paragraph.text)
	except:
		print('lol')


pprint(content)
'''
f = open("C:/Users/Rohan/Desktop/test.txt", 'a')
for c in content:
	f.write(str(c))
f.close()
 '''