import requests
from bs4 import BeautifulSoup
from datetime import datetime

SOURCE_NAME = "MDPI"

MDPI_URL = "https://www.mdpi.com/search?sort=pubdate&page_count=100&view=default"

def getContent(article_div):
    abstract_div = article_div.find("div", class_="abstract-cropped inline")
    if abstract_div:
        return abstract_div.get_text(strip=True)
    return ""

def Scrape_mdpi(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error al obtener la página: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    posts = []
    articles = soup.find_all("div", class_="generic-item article-item")

    for article in articles:
        try:
            # Título y URL
            content_div = article.find("div", class_="article-content")
            link_tag = content_div.find("a", class_="title-link")
            title = link_tag.text.strip()
            paper_url = "https://www.mdpi.com" + link_tag["href"]

            # Contenido del abstract
            content = getContent(article)

            post = {
                'title': title,
                'summary': content[:200] + "...",  # primer fragmento como resumen
                'content': content,
                'url': paper_url,
                'type': "paper",
                'published_at': datetime.now(),
                'sourcename': SOURCE_NAME
            }

            posts.append(post)

            if len(posts) == 20:
                break

        except Exception as e:
            print(f"Error procesando un artículo: {e}")
            continue

    return posts

if __name__ == "__main__":
    posts = Scrape_mdpi(MDPI_URL)
    for post in posts:
        print(post)
