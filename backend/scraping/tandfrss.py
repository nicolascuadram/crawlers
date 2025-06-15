import feedparser
from bs4 import BeautifulSoup
from datetime import datetime

SOURCE_NAME = "Taylor & Francis"

def scrape_tandf_rss(rss_url):
    feed = feedparser.parse(rss_url)
    print("########COMIENZO")
    print(feed.entries[0])
    print("########FINAL")
    posts = []

    for entry in feed.entries[:20]:  # Solo los primeros 20
        content_html = entry.content[0]['value'] if 'content' in entry else ''
        soup = BeautifulSoup(content_html, 'html.parser')

        # Buscar línea con palabras clave
        keywords = ""
        for p in soup.find_all("p"):
            if "keywords" in p.text.lower():
                keywords = p.text.strip()
                break

        post = {
            'title': entry.title,
            'summary': keywords,  # Aquí ahora van las palabras clave
            'content': content_html,
            'url': entry.link,
            'type': "paper",
            'published_at': entry.published if 'published' in entry else '',
            'sourcename': SOURCE_NAME,
            'downloadArticleLink': entry.link,
            'authors': [a['name'] for a in entry.authors] if 'authors' in entry else [entry.author] if 'author' in entry else []
        }
        posts.append(post)

    return posts

# Ejemplo de uso
rss_url = "https://www.tandfonline.com/action/showFeed?type=etoc&feed=rss&jc=tcph20"  # Reemplaza con el RSS de la revista deseada
posts = scrape_tandf_rss(rss_url)
for post in posts:
    print(post)
