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
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

def sanitize_filename(title):
    filename = re.sub(r'[:?!]', '_', title)
    filename = filename.replace(' ', '_')
    return filename

def sanitize_value(value):
    if value is None:
        return None
    value = str(value).replace('\n', ' ').replace('"', '\\"')
    return f'"{value}"'

cur = conn.cursor()
cur.execute("SELECT id, title, summary, content, url, type, published_at, created_at, log_id, sourcename FROM post")
rows = cur.fetchall()

output_dir = "../frontend/src/content/blog"
os.makedirs(output_dir, exist_ok=True)

for row in rows:
    (id, title, summary, content, url, type_, published_at, created_at, log_id, sourcename) = row

    safe_title = title.replace(" ", "_").replace("/", "_") if title else f"post_{id}"
    filename = f"{sanitize_filename(safe_title)}.md"
    filepath = os.path.join(output_dir, filename)

    if os.path.exists(filepath):
        print(f"Archivo ya existe, omitido: {filepath}")
        continue

    markdown_content = f"""---
title: {sanitize_value(title) or ''}
description: {sanitize_value(summary) or ''}
url: {sanitize_value(url) or ''}
type: {sanitize_value(type_) or ''}
pubDate: {sanitize_value(published_at) or ''}
created_at: {sanitize_value(created_at) or ''}
log_id: {log_id or ''}
sourcename: {sourcename or ''}
author: {'pendiente' or ''}
heroImage: '/blog-placeholder-5.jpg'
---

{content or ''}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Archivo generado: {filepath}")

cur.close()
conn.close()
