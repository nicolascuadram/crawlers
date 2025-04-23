from bs4 import BeautifulSoup
import requests

url : str = "https://urzuaf.github.io/blog-gpt/"

req = requests.get(url)

soup = BeautifulSoup(req.text, features="lxml")
enlaces = soup.find_all("a")
nuevosEnlaces = []

titles = []
content = []

for enlace in enlaces:
    nuevosEnlaces.append(enlace.get("href"))

for nenlace in nuevosEnlaces:
    req = requests.get(url + "/" + nenlace)
    soup = BeautifulSoup(req.text)
    title = soup.find("title")
    article = soup.find("article")
    titles.append(title)
    content.append(article)

i = 0
while (i < len(titles)):
    print(titles[i])
    print(content[i])
    i += 1
