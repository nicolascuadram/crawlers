import feedparser
from datetime import datetime

SOURCE_NAME = "MDPI"
# RSS con artículos más recientes de todas las revistas
MDPI_RSS_URL = "https://www.mdpi.com/rss?sort=pubdate&page_count=100&view=default"

def Scrape_mdpi(url: str):
    feed = feedparser.parse(url)
    #print(feed.entries[0])
    posts = []

    for entry in feed.entries[:20]:  # Solo los primeros 20
        post = {
            'title': entry.title,
            'summary': entry.prism_publicationname if 'prism_publicationname'in entry else '',
            'content': entry.summary if 'summary' in entry else '',
            'url': entry.link,
            'type': "paper",
            'published_at': entry.published if 'published' in entry else '',
            'sourcename': SOURCE_NAME,
            'downloadArticleLink': entry.id, 
            'authors': [a['name'] for a in entry.authors] if 'authors' in entry else [entry.author] if 'author' in entry else []
        }
        posts.append(post)

    return posts

if __name__ == "__main__":
    posts = Scrape_mdpi(MDPI_RSS_URL)
    for post in posts:
        #print(post)
        pass
