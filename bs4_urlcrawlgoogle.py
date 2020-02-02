import bs4 as bs 
import urllib.request
import requests
from pprint import pprint


keyword = "Cloud Computing"
keyword = keyword.replace(" ", "+")

link = "https://www.google.dz/search?q=" + keyword
source = requests.get(link)
soup = bs.BeautifulSoup(source.content, 'lxml')

links = soup.findAll("a")

urls = []
for url in links:
	if "/url?q=" in str(url.get('href')):
		urls.append(str(url.get('href')).strip("/url?q="))

urls_clean = [str(urls[i])[0:str(urls[i]).find("&sa")] for i in range(len(urls))]
urls_clean.pop(len(urls_clean)-1)

print("Links Found: " + str(len(urls_clean)))

content = []
i=0
for url in urls_clean:
	i = i+1
	try:
		source2 = urllib.request.urlopen(url).read()
		soup = bs.BeautifulSoup(source2, 'lxml')
		for paragraph in soup.find_all('p'):
			content.append(str(paragraph.text).strip())
	except:
		print("Link Number: "+str(i)+" is Forbidden")

keyword = keyword.replace("+", " ")
with open("C:/Users/Rohan/Desktop/Tests/"+keyword+".txt", 'a', encoding = 'utf-8') as f:
	for para in content:
		f.write(str(para))

print("Finished Writing.")