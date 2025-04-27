from bs4 import BeautifulSoup
import requests

url : str = "https://arxiv.org/abs/arXiv:2504.17788"

req = requests.get(url)

soup = BeautifulSoup(req.text, features="lxml")
sp = soup.find('blockquote')
sp2 = soup.find('div', class_="dateline")
content = sp.text.strip() if sp else ''
date = sp2.text.strip() if sp2 else ''
print(content, date)