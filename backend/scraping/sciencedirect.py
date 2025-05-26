import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin

BASE_URL = "https://www.sciencedirect.com"
SOURCE_NAME = "ScienceDirect Journal"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

def Scrape_sciencedirect(url: str):
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error al obtener página principal: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    posts = []

    # Encontrar todos los artículos dentro de la lista
    article_list = soup.find("ol", class_="article-list")
    if not article_list:
        print("❌ No se encontró la lista de artículos")
        return []

    articles = article_list.find_all("li", class_="js-article-list-item")
    for article in articles:
        try:
            content_div = article.find("div", class_="js-article article-content")
            if not content_div:
                continue

            # Título
            title_tag = content_div.find("h2")
            title = title_tag.get_text(strip=True) if title_tag else "Sin título"

            # Link del artículo
            link_tag = content_div.find("a", href=True)
            href = link_tag["href"] if link_tag else ""
            full_url = urljoin(BASE_URL, href)

            # Obtener el abstract desde la página individual
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

    # Buscar el abstract dentro de la clase específica
    abstract_div = soup.find("div", class_="js-abstract-body-text branded")
    if not abstract_div:
        return "Resumen no disponible"

    return abstract_div.get_text(strip=True)
