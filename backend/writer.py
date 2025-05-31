import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import re

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

conn = psycopg2.connect(
    host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
)


def sanitize_filename(title):
    filename = re.sub(r"[:?!]", "_", title)
    filename = filename.replace(" ", "_")
    return filename


def sanitize_value(value):
    if value is None:
        return None
    value = str(value).replace("\n", " ").replace('"', '\\"')
    return f'"{value}"'


cur = conn.cursor()
cur.execute(
    "SELECT id, title, summary, content, url, type, published_at, created_at, log_id, sourcename, downloadArticleLink, authors FROM post"
)
rows = cur.fetchall()

output_dir = "../frontend/src/content/blog"
os.makedirs(output_dir, exist_ok=True)

for row in rows:
    (
        id,
        title,
        summary,
        content,
        url,
        type_,
        published_at,
        created_at,
        log_id,
        sourcename,
        downloadArticleLink,
        authors,
    ) = row

    safe_title = title.replace(" ", "_").replace("/", "_") if title else f"post_{id}"
    filename = f"post{id}.md"
    filepath = os.path.join(output_dir, filename)

    if os.path.exists(filepath):
        print(f"Archivo ya existe, omitido: {filepath}")
        continue

    if title is None or title.strip() == "":
        print(f"Post sin título, omitido: {filepath}")
        continue

    if summary is None or summary.strip() == "":
        print(f"Post sin resumen, omitido: {filepath}")
        continue
    if content is None or content.strip() == "":
        print(f"Post sin contenido, omitido: {filepath}")
        continue

    heroImage = ""
    if sourcename == "Revista Iberoamericana de Educación":
        heroImage = "/revista.jpg"
    if sourcename == "arXiv CS":
        heroImage = "/arxiv.jpg"
    if sourcename == "MDPI":
        heroImage = "/mdpi.jpg"

    markdown_content = f"""---
title: {sanitize_value(title) or ""}
description: {sanitize_value(summary) or ""}
url: {sanitize_value(url) or ""}
type: {sanitize_value(type_) or ""}
pubDate: {sanitize_value(published_at) or ""}
created_at: {sanitize_value(created_at) or ""}
log_id: {log_id or ""}
sourcename: {sourcename or ""}
author: {authors or ""}
heroImage: {heroImage or "/blog-placeholder-3.jpg"}
linkDownload: {sanitize_value(downloadArticleLink) or ""}
---

{content or ""}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Archivo generado: {filepath}")

cur.close()
conn.close()
