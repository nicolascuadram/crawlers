import requests 
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin

BASE_URL = "https://www.tandfonline.com"
SOURCE_NAME = "TANDF"

# Cabeceras para simular navegador real
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive"
}

def Scrape_tandf(url: str):
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error al obtener página principal: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    posts = []

    articles = soup.find_all("div", class_="articleEntry")
    for article in articles:
        try:
            title_div = article.find("div", class_="art_title")
            if not title_div:
                continue

            link_tag = title_div.find("a", href=True)
            if not link_tag:
                continue

            title = link_tag.get_text(strip=True)
            href = link_tag["href"]
            full_url = urljoin(BASE_URL, href)

            # Extraer abstract desde la página del artículo
            abstract = get_abstract(full_url)

            post = {
                "title": title,
                "summary": abstract[:200] + "...",
                "content": abstract,
                "url": full_url,
                "type": "paper",
                "published_at": datetime.now(),
                "sourcename": SOURCE_NAME
            }

            posts.append(post)

        except Exception as e:
            print(f"❌ Error procesando artículo: {e}")
            continue

    return posts


def get_abstract(article_url):
    response = requests.get(article_url, headers=HEADERS)
    if response.status_code != 200:
        print(f"❌ Error al acceder al artículo: {article_url}")
        return "Resumen no disponible"

    soup = BeautifulSoup(response.content, "html.parser")

    # Buscar el div con clase hlFld-Abstract y su párrafo
    abstract_div = soup.find("div", class_="hlFld-Abstract")
    if not abstract_div:
        return "Resumen no disponible"

    paragraph = abstract_div.find("p")
    return paragraph.get_text(strip=True) if paragraph else "Resumen no disponible"
