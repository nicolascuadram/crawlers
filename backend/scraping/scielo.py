from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

SOURCE_NAME = "SciELO Chile"

def init_firefox_driver():
    options = Options()
    options.headless = True# Cambiar a True para que no se abra la ventana
    return webdriver.Firefox(options=options)

def scrape_scielo(journal_url):
    driver = init_firefox_driver()
    driver.get(journal_url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Artículos: están dentro de la segunda o tercera tabla grande
    all_tables = soup.find_all("table")
    
    #print(all_tables[3], len(all_tables))
    html = all_tables[3]
    soup = html

    # Lista para almacenar los resultados
    papers = []

    # Cada artículo está en un <td> que contiene el nombre del paper en <b>, luego autores y luego un div con links
    for td in soup.find_all("td"):
        b_tag = td.find("b")
        if b_tag:
            paper_title = b_tag.get_text(strip=True)
            
            # Autores: todos los <a> que están justo después del <b>
            # Se asume que los autores están en el siguiente <font> con clase normal y conteniendo enlaces <a>
            authors_font = b_tag.find_next_sibling("font", class_="normal")
            if not authors_font:
                # A veces puede no estar, intentar buscar en td directamente
                authors_font = td.find_all("font", class_="normal")
                authors = []
                for f in authors_font:
                    authors += [a.get_text(strip=True) for a in f.find_all("a")]
                authors_str = ", ".join(authors)
            else:
                authors_links = authors_font.find_all("a")
                authors_str = ", ".join([a.get_text(strip=True) for a in authors_links])
            
            # Links: dentro del div siguiente que contenga enlaces
            div_links = td.find("div", align="left")
            if div_links:
                # Link resumen en español
                resumen_es = None
                pdf_link = None
                # Buscar el link cuyo texto contenga "resumen en Español"
                resumen_a = None
                for a_tag in div_links.find_all("a"):
                    href = a_tag.get('href', '')
                    texto = (a_tag.get_text() or '').strip().lower()
                    if "sci_abstract" in href and "lng=es" in href:
                        resumen_a = a_tag
                    break
                if resumen_a:
                    resumen_es = resumen_a['href']
                # Buscar link pdf, imagen alt="pdf"
                pdf_a = div_links.find("a", href=lambda href: href and href.endswith(".pdf"))
                if pdf_a:
                    pdf_link = pdf_a['href']
                
                # Guardar como strings (o None si no se encuentran)
                papers.append({
                    "nombre_paper": paper_title,
                    "autores": authors_str,
                    "link_pdf": 'https://www.scielo.cl'+pdf_link,
                    "link_resumen_es": resumen_es
                })

    posts = []
    for p in papers:
        resumen_url = p["link_resumen_es"]
        if resumen_url:
            driver.get(resumen_url)
            # Esperar que cargue el div con clase 'index,es' (asumiendo que es único)
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'index,es')]"))
                )
                # Obtener el div
                div_html = driver.find_element(By.XPATH, "//*[contains(@class, 'index,es')]").get_attribute("outerHTML")
                soup = BeautifulSoup(div_html, "html.parser")

                # Extraer palabras clave: <p><strong>Palabras clave</strong>: ... </p>
                keywords = ""
                p_tags = soup.find_all("p")
                for ptag in p_tags:
                    strong_tag = ptag.find("strong")
                    if strong_tag and "palabras clave" in strong_tag.get_text(strip=True).lower():
                        # Obtener texto quitando "Palabras clave :" y espacios
                        keywords = ptag.get_text(separator=" ", strip=True)
                        # Remover la parte "Palabras clave :" para quedarnos solo con las keywords
                        keywords = keywords.lower().replace("palabras clave :", "").strip()
                        break

                # Extraer abstract: buscar el primer <p> que no contenga "Palabras clave" ni esté vacío ni solo espacios
                abstract = ""
                for ptag in p_tags:
                    txt = ptag.get_text(strip=True)
                    if txt and "palabras clave" not in txt.lower():
                        abstract = txt

                # Armar lista de autores como lista, separando por coma y eliminando espacios extra
                lista_autores = [a.strip() for a in p["autores"].split(",")]

                post = {
                    'title': p["nombre_paper"],
                    'summary': keywords,
                    'content': abstract,
                    'url': resumen_url,
                    'type': "paper",
                    'published_at': '',
                    'sourcename': 'scielo',
                    'downloadArticleLink': p["link_pdf"],
                    'authors': lista_autores
                }
                posts.append(post)
            except Exception as e:
                print(f"No se pudo obtener el div 'index,es' para {p['nombre_paper']}: {e}")



    # Mostrar resultados

    driver.quit()
    return posts

if __name__ == "__main__":
    journal_url = "https://www.scielo.cl/scielo.php?script=sci_issuetoc&pid=0718-500620250002&lng=es&nrm=iso"
    posts = scrape_scielo(journal_url)

    for post in posts:
        print(post)
