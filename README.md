# Sistema Unificado de Extracción de Información para el Curso de Gestión de Proyectos Tecnológicos

## Instalación del sistema en local

### Requisitos

- node
- python
- npm
- pip
- postgreSQL

### Paso 1: Clonar el repositorio

`git clone https://github.com/nicolascuadram/crawlers.git`

### Paso 2: Instalación de dependencias

Una vez descargado el código fuente debemos instalar las librerias necesarias para ejecutar el sistema

#### Backend

Ingresamos a la carpeta contenedora del backend e instalamos las dependencias mendiante `pip`

`pip install -r requirements.txt`

#### Frontend

Ingresamos a la carpeta contenedora del frontend e instalamos las dependencias mediante `npm`

`npm install`

### Paso 3: Ejecución

#### Frontend

Dentro de la carpeta contenedora del frontend se debe iniciar el servicio con el comando `npm run dev`, esto levantará el servicio en el puerto por defecto 4321, que permitirá acceder a los posts guardados en la aplicación, dichos posts se encuentran en la carpeta src/content/blog y siguen un formato en especifico.

#### Backend

Para la correcta ejecución del backend se necesita un archivo llamado `.env` ubicado en la carpeta contenedora, es decir, en: `backend/.env`
dicho archivo debe contener los siguientes datos de configuración de el SGBD postgreSQL:

```conf
DB_NAME=nombrebd
DB_USER=usuariobd
DB_PASSWORD=passwordbd
DB_HOST=hostbd
DB_PORT=puertobd
```

#### Base de datos

Se debe crear una base de datos en postgreSQL, esta debe inicializarse con la estructura ubicada en `db/crawlersbd.sql`

#### Scraping

El backend cuenta con 2 scripts de python, los cuales manejan la lógica de la aplicación

- `crawler.py` se encarga de ejecutar el scraping, extrayendo la información de todas las fuentes y guardandolas en la base de datos.
- `writer.py` toma la información de la base de datos y la escribe en archivos .md, los cuales se renderizarán posteriormente en el frontend

Por lo tanto para agregar nuevas fuentes deben correrse secuencialmente ambos archivos.

En entornos linux se puede hacer uso del script `backend/entrypoint.sh` el cual ejecutará programará ambos scripts para correr automaticamente cada 4 horas.

##### Importante

Se debe modificar el archivo `writer.py` para guardar los archivos en la ruta correcta, por defecto está seteado a

```python
output_dir = "/app/content"
```

este valor funciona para la aplicación dockerizada, en caso de querer leventarla en local, se debe modificar a la carpeta donde se guardarán los posts, que en la mayoria de los casos seria:

```python
output_dir = "../frontend/src/content/blog"
```

## Instalación Dockerizada

Para la ejecución de la aplicación dockerizada, basta con comprobar que el archivo .env ubicado en el backend, coincida con las credenciales de bases de datos definidas en el docker-compose, este archivo debe tener la siguiente estructura (reemplazar con los valores reales)

```conf
DB_NAME=crawlers
DB_USER=furzua
DB_PASSWORD=1234
DB_HOST=dbcrawl
DB_PORT=5432
```

Posteriormente se deben instalar las dependencias en la carpeta del frontend 

```bash
cd frontend && npm i && cd ..
```

Finalmente, se puede desplegar la aplicación con el comando

```bash
sudo docker compose up --build
````

## Agregar una nueva fuente de scraping

Este sistema permite la integración de nuevas fuentes de artículos académicos o técnicos mediante scrapers personalizados. La arquitectura está diseñada para ser modular y extensible.

### 🧱 Estructura del sistema

    backend/scraping/: Carpeta que contiene los scrapers individuales por fuente.

    backend/crawler.py : Archivo principal que coordina la ejecución de scrapers.

    Base de datos PostgreSQL con las tablas: source, post, log.

### ✅ Requisitos para agregar una nueva fuente

#### Paso 1: Agregar la fuente a la base de datos

Ejecuta un INSERT INTO en la tabla source para registrar la nueva fuente:

```sql
INSERT INTO source (id, name, url, type, active, created_at)
VALUES (6, 'Nombre de la nueva fuente', 'https://url-de-la-fuente.com', 'article', true, CURRENT_TIMESTAMP);
```

    - id: Valor único.

    - name: Nombre que usarás también para el routing del scraper.

    - url: URL de origen para scrapear.

    - type: Tipo de contenido de la fuente, por ejemplo, articulos.

    - active: true para que se ejecute.

    - created_at: CURRENT_TIMESTAMP.

#### Paso 2: Crear el scraper

Dentro del directorio backend/scraping/, crea un nuevo archivo, por ejemplo:

`scraping/nueva_fuente.py`

Ejemplo básico de scraper (retorna lista de post):

```python
import request
from bs4 import BeautifulSoup

def scrape_nueva_fuente(base_url):
    posts = []

    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for item in soup.select(".post"):  # Ajustar al selector real
        post = {
            'title': item.select_one(".title").get_text(strip=True),
            'summary': item.select_one(".keywords").get_text(strip=True),
            'content': item.select_one(".abstract").get_text(strip=True),
            'url': item.select_one(".doi a")["href"],
            'type': 'article',
            'published_at': item.select_one(".date").get_text(strip=True),
            'sourcename': 'Nombre de la nueva fuente',
            'downloadArticleLink': item.select_one(".pdf a")["href"],
            'authors': ", ".join([a.get_text(strip=True) for a in item.select(".authors span")])
        }
        posts.append(post)

    return posts
```

La lógica o librerias a usar en el scraping pueden variar para cada fuente, pero es necesario que la función usada para scrapear, reciba como argumento solo la url objetivo y retorne un arreglo de objetos con la siguiente estructura:

```python
post = {
            'title': string, # titulo de los articulos
            'summary': string, # palabras claves de los articulos
            'content': string, # abstract del articulo
            'url': string, # link a la pagina del articulo DOI
            'type': string, # article, paper, etc
            'published_at': string, # fecha de publicacion
            'sourcename': string, # Nombre de la fuente de los posts
            'downloadArticleLink': string, # link para descargar el pdf o de no haberlo el doi nuevamente
            'authors': string # lista de autores del articulo
        }

```

#### Paso 3: Importar el scraper

Ve al archivo principal de scraping (crawler.py) y agrega la importación:

`from scraping.nueva_fuente import scrape_nueva_fuente`

#### Paso 4: Agregarlo al router de scrapers

Dentro de la función `scrape_source`, añade el if correspondiente usando el nombre registrado en la base de datos:

```python
if source_name.lower() == 'nombre de la nueva fuente':
    return scrape_nueva_fuente(source_url)
```

Asegúrate de que el texto de comparación (source_name.lower()) coincida exactamente con el campo name en la base de datos en minúsculas.

##### 📦 Formato esperado de cada post

Cada scraper debe devolver una lista de diccionarios con la siguiente estructura:

```python
post = {
    'title': string,               # Título del artículo
    'summary': string,             # Palabras clave
    'content': string,             # Resumen / Abstract
    'url': string,                 # URL del artículo (preferentemente DOI)
    'type': string,                # Tipo de publicación (ej. "article")
    'published_at': string,        # Fecha de publicación (ISO 8601 preferido)
    'sourcename': string,          # Nombre de la fuente (debe coincidir con source.name)
    'downloadArticleLink': string,# Link de descarga (PDF o DOI)
    'authors': string              # Autores, separados por coma
}
```

🧪 Recomendaciones - Valida la existencia de campos antes de extraerlos para evitar errores (NoneType). - Loguea errores si una página no contiene lo esperado. - Testea manualmente el scraper antes de habilitarlo en producción. - Usa try/except dentro del scraper si es una fuente inconsistente.

🧹 Opcional: desactivar temporalmente una fuente

`UPDATE source SET active = false WHERE name = 'Nombre de la fuente';`
