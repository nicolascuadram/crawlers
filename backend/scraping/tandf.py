from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import requests

SOURCE_NAME = "Taylor & Francis"

def init_firefox_driver():
    options = Options()
    options.headless = True# Muy importante para correr sin interfaz gráfica
    return webdriver.Firefox(options=options)


def getAbstract(doi):
    url = f"https://www.tandfonline.com/pb/widgets/ajax/graphql/abstracts?type=abstract&doi={doi}&pbContext=;subPage:string:Topic Landing Page;taxonomy:taxonomy:allsubjects;topic:topic:allsubjects>cm;page:string:Search Result;wgroup:string:Publication Websites;pageGroup:string:Search Flow;website:website:TFOPB&widgetId=7e3f7864-5ba2-489e-8645-be774ad94f6b"
    driver = init_firefox_driver()
    driver.get(url)
    try:
        # Espera a que el abstract se cargue
        WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.CLASS_NAME, "abstractSection"))
        )
        abstract_div = driver.find_element(By.CLASS_NAME, "abstractSection")
        abstract = abstract_div.text.strip()
    except Exception as e:
        print("No se pudo obtener el abstract:", e)
        abstract = ""
    driver.quit()
    return abstract

def scrape_tandf(journal_url):
    driver = init_firefox_driver()
    driver.get(journal_url)
    time.sleep(5)

    articles = driver.find_elements(By.CSS_SELECTOR, 'article.searchResultItem')[:8]
    posts = []

    for article in articles:
        try:
            soup = BeautifulSoup(article.get_attribute('outerHTML'), 'html.parser')

            # Título y URL
            title_tag = soup.find('div', class_='art_title').find('a', class_='ref nowrap')
            title = title_tag.get_text(strip=True)
            url = "https://www.tandfonline.com" + title_tag['href']

            # Autores
            authors_tag = soup.find('div', class_='author')
            authors_text = authors_tag.get_text(strip=True) if authors_tag else ""


            # Fecha de publicación
            pub_metas = soup.find_all('div', class_='publication-meta')
            published_at = ""
            summary = ""
            if len(pub_metas) >= 2:
                published_at = pub_metas[1].get_text(strip=True)
            #Tags
                summary = pub_metas[0].get_text(strip=True)

            # DOI
            doi = url.split("/doi/full/")[1] if "/doi/full/" in url else ""

            content = getAbstract(doi)

        except Exception as e:
            print(f"Error procesando artículo: {e}")
            continue

        post = {
            'title': title,
            'summary': summary,
            'content': content,
            'url': url,
            'type': "paper",
            'published_at': published_at,
            'sourcename': SOURCE_NAME,
            'downloadArticleLink': url,
            'authors': authors_text,
        }
        posts.append(post)

    driver.quit()
    return posts

if __name__ == "__main__":
# Ejemplo de uso
    journal_url = "https://www.tandfonline.com/subjects/computer-science?startPage=&target=default&content=standard"
    posts = scrape_tandf(journal_url)

    for post in posts:
        print(post)
