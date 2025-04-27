import requests
from bs4 import BeautifulSoup
from datetime import datetime
from utils.htmltomd import html_to_markdown

SOURCE_NAME = "Dev to"


def getContent(url : str) -> str:
    if url == '':
        return ''

    req = requests.get(url)
    soup = BeautifulSoup(req.text, features="lxml")
    content = soup.find('div', id="article-body")
    #content = content.text.strip() if content else ''

    return html_to_markdown(content)


def Scrape_dev_to(url:str):
    
    req = requests.get(url)

    soup = BeautifulSoup(req.text, features="lxml")
    scraping = soup.find_all('div', class_ = "crayons-story__body")
    posts = []

    for c in scraping:

        header = c.find('h2', class_="crayons-story__title")
        if header:
            a_tag = header.find('a')
            if a_tag:
                link = a_tag['href']
                title = a_tag.text.strip()
            else:
                link = ''
                title = ''
        else:
            link = ''
            title = ''

        sum = c.find('div', class_="crayons-story__tags")
        sums = []
        if sum:
            for a_tag in sum.find_all('a'):
                tag_text = a_tag.get_text(strip=True).replace('#', '')
                sums.append(tag_text)
            summary = ', '.join(sums)
        else:
            summary = ''
        
        contenido = getContent(link)


        type = "Blog"

        fecha = c.find('a', class_="crayons-story__tertiary fs-xs")
        if fecha:
            time_tag = fecha.find('time')
            if time_tag:
                datetime_value = time_tag['datetime']
                date_only = datetime_value.split('T')[0]
                fecha = date_only
            else:
                fecha = ''
        else:
            fecha = None

        post = {
                'title': title,
                'summary': summary,
                'content': contenido,
                'url': link,
                'type': type,
                'published_at': fecha,
                'sourcename': SOURCE_NAME
            }

        posts.append(post)


    return posts