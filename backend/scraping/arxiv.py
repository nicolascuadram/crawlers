import requests
from bs4 import BeautifulSoup
from datetime import datetime


# ARXIV_URL = "https://arxiv.org/list/cs/recent"
SOURCE_NAME = "arXiv CS"


def Scrape_arxiv(ARXIV_URL: str):
    response = requests.get(ARXIV_URL)
    if response.status_code != 200:
        print(f"Error al obtener la página: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    # Buscar las entradas
    entries = soup.find_all("dt")
    details = soup.find_all("dd")

    posts = []

    for dt, dd in zip(entries, details):
        try:
            # Link al artículo
            link_tag = dt.find("a", title="Abstract")
            paper_id = link_tag.text.strip()
            paper_url = f"https://arxiv.org/abs/{paper_id}"

            # Título
            title_tag = dd.find("div", class_="list-title mathjax")
            title = title_tag.text.replace("Title:", "").strip()

            # Resumen
            summary_tag = dd.find("div", class_="list-subjects")
            summary = summary_tag.text.strip() if summary_tag else ""
            summary = summary.split("\n")[1]

            # Content: para simplificar pondremos el summary (puedes expandirlo después)
            contents = getContent(url=paper_url)

            # Tipo: lo dejamos como "paper"
            paper_type = "paper"

            # Fecha de publicación: no está directamente aquí, así que ponemos hoy
            published_at = "pendiente"

            post = {
                "title": title,
                "summary": summary,
                "content": contents[0],
                "url": paper_url,
                "type": paper_type,
                "authors": contents[1],
                "downloadArticleLink": "https://arxiv.org" + contents[2],
                "published_at": contents[3],
                "sourcename": SOURCE_NAME,
            }

            posts.append(post)

            # Solo buscar en los ultimos 20 posts
            if len(posts) == 10:
                break
        except Exception as e:
            print(f"Error procesando un post: {e}")
            continue

    return posts


# Para obtener el contenido debemos abrir el link de cada articulo y scrapearlo a el en especifico
def getContent(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error al obtener la página: {response.status_code}")
        return ""
    soup = BeautifulSoup(response.content, "html.parser")
    bq = soup.find("blockquote")
    content = bq.text.strip() if bq else ""
    authors = (
        soup.find("div", class_="authors").text.strip()
        if soup.find("div", class_="authors")
        else ""
    )
    downloadArticleLink = (
        soup.find("a", class_="download-pdf")["href"]
        if soup.find("a", class_="download-pdf")
        else ""
    )
    published_at = (
        soup.find("div", class_="dateline").text.strip()
        if soup.find("div", class_="dateline")
        else ""
    )
    return [content, authors, downloadArticleLink, published_at]


if __name__ == "__main__":
    posts = Scrape_arxiv()
    print(f"Recibidos {posts}")
