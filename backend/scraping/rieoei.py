import requests
from selectolax.parser import HTMLParser
from datetime import datetime
from utils.htmltomd import html_to_markdown_selectolax

SOURCE_NAME = "Revista Iberoamericana de Educación"

def Scrape_rieoei(RIEOEI_URL: str, limite_revistas: int = 3):
    session = requests.Session()
    session.headers.update({               # un User-Agent decente evita bloqueos tontos
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0 Safari/537.36"
        )
    })
    response = session.get(RIEOEI_URL, timeout=15)
    posts = []
    if response.status_code != 200:
        print(f"Error al obtener la página: {response.status_code}")
        return []

    html = HTMLParser(response.text)

    #buscar los links de las revistas
    revistas_links = []
    rinks = html.css('a.cover')
    for link in rinks:
        revistas_links.append((link.attributes['href']))

    for link in revistas_links[:limite_revistas]:
        response = session.get(link)
        if response.status_code != 200:
            print(f"Error al obtener la página: {response.status_code}")
            return []
        html = HTMLParser(response.text)



        # Buscar todos los bloques de artículos
        article_divs = html.css('div.obj_article_summary')

        html_links = []

        for div in article_divs:
            # Buscar el enlace al archivo HTML (no PDF)
            html_link_tag = div.css_first('a.obj_galley_link.file')
            if html_link_tag and 'href' in html_link_tag.attributes:
                html_href = html_link_tag.attributes['href']
                html_links.append(html_href)

        # Mostrar resultados
        for link in html_links:
            posts.append(follow_link(link, session))

    return posts

def follow_link(link: str, session) -> str:
    response = session.get(link)
    if response.status_code != 200:
        print(f"Error al obtener la página: {response.status_code}")
        return ''
    html = HTMLParser(response.text)

    iframe_node = html.css_first("iframe")
    iframe_src = iframe_node.attributes["src"].strip()

    html = HTMLParser(session.get(iframe_src).text)

    title = ''
    summary = ''
    content = ''
    published_at = ''
    authors = ''
    downloadArticleLink = ''

    title_tag = html.css_first('p.RIE-Titular')
    if title_tag:
        if title_tag:
            title = title_tag.text(strip=True)
    
    autor_tag = html.css_first('p.RIE-Autor')
    if autor_tag:
        autor = autor_tag.text(strip=True)
        autor = autor.split('http')[0]
        authors = autor
    
    summary_tag = html.css_first('p.RIE-S-ntesis1')
    if summary_tag:
        summary = summary_tag.text(strip=True)
    
    # content_tag = html.css_first('p.RIE-T-tulo1-Inicio')
    # print(content_tag)
    # if content_tag:
    #     collected_html = []
    #     node = content_tag
    #     while node:
    #         collected_html.append(node.html)
    #         node = node.next
    #     rawhtml = ''.join(collected_html)
    #     selected_html = HTMLParser(rawhtml).root
    #     print(selected_html)
    #     content = html_to_markdown_selectolax(selected_html)
    #     #content = selected_html.text(strip=True)
    #     #print(content[:500])


    published_at_tag = html.css('p.RIE-MID')
    if published_at_tag:
        published_at = published_at_tag[-1].text(strip=True)
        published_at = published_at.split(';')[0]
        published_at = published_at.split(':')[1]

    post = {
        'title': title,
        'summary': summary,
        'content': content,
        'url': link,
        'type': 'paper',
        'published_at': published_at,
        'sourcename': SOURCE_NAME,
        'downloadArticleLink': downloadArticleLink,
        'authors': authors
        } 
    
    return post
        

if __name__ == "__main__":
    posts = Scrape_rieoei('https://rieoei.org/RIE/issue/archive', limite_revistas=3)
    for post in posts:
        print(f"{post['title']} -> {post['url']}")
        print(post)
