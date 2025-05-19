import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
from scraping.arxiv import Scrape_arxiv
from scraping.devto import Scrape_dev_to
from scraping.rieoei import Scrape_rieoei

# Cargar las variables de entorno
load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Conexión
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")
        return None

# Obtener las fuentes activas
def get_active_sources(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, url, type FROM source WHERE active = TRUE")
    sources = cursor.fetchall()
    cursor.close()
    return sources

# Insertar un log
def insert_log(conn, source_id, error_message=None):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO log (source_id, fetched_at, error_message)
        VALUES (%s, NOW(), %s)
        RETURNING id
    """, (source_id, error_message))
    log_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    return log_id

# Guardar posts
def save_posts(conn, posts, log_id):
    cursor = conn.cursor()
    for post in posts:
        try:
            # Verificar si ya existen posts con el mismo título
            cursor.execute("SELECT id FROM post WHERE title = %s", (post['title'],))
            exists = cursor.fetchone()

            if exists:
                print(f"Post ya existe: {post['title']}")
                continue

            # Insertar el nuevo post
            cursor.execute("""
                INSERT INTO post (title, summary, content, url, type, published_at, created_at, log_id, sourcename, downloadArticleLink, authors)
                VALUES (%s, %s, %s, %s, %s, %s, NOW(), %s, %s, %s, %s)
            """, (
                post['title'],
                post['summary'],
                post['content'],
                post['url'],
                post['type'],
                post['published_at'],
                log_id,
                post['sourcename'],
                post['downloadArticleLink'],
                post['authors']
            ))
        except Exception as e:
            print(f"Error insertando un post: {e}")
            conn.rollback()
            continue
    conn.commit()
    cursor.close()

# Asociar el scraping al nombre de la fuente
def scrape_source(source_name, source_url):
    if source_name.lower() == 'arxiv cs':
        return Scrape_arxiv(source_url)
    if source_name.lower() == 'dev to':
        return Scrape_dev_to(source_url)
    if source_name.lower() == 'revista iberoamericana de educación':
        return Scrape_rieoei(source_url)
    else:
        print(f"No hay scraper configurado para {source_name.lower()} ")
        return []

def main():
    conn = connect_db()
    if conn is None:
        print("No se pudo conectar a la base de datos.")
        return

    sources = get_active_sources(conn)
    if not sources:
        print("No hay fuentes activas.")
        conn.close()
        return

    for source_id, source_name, source_url, source_type in sources:
        print(f"Scrapeando fuente: {source_name} ({source_url})")
        try:
            posts = scrape_source(source_name, source_url)
            log_id = insert_log(conn, source_id)
            if posts:
                save_posts(conn, posts, log_id)
                print(f"{len(posts)} posts guardados para {source_name}")
            else:
                print(f"No se encontraron posts en {source_name}")
        except Exception as e:
            print(f"Error procesando {source_name}: {e}")
            # Si falla todo, igual insertamos el log con error
            insert_log(conn, source_id, error_message=str(e))

    conn.close()
    print("Scraping finalizado.")

if __name__ == "__main__":
    main()
