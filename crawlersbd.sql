CREATE TABLE IF NOT EXISTS source (
  id serial PRIMARY KEY,
  name text,
  url text,
  type text,
  active boolean,
  created_at timestamp
);


CREATE TABLE IF NOT EXISTS log (
  id serial PRIMARY KEY,
  source_id integer references source(id) on delete cascade on update cascade,
  fetched_at timestamp,
  error_message text
);

CREATE TABLE IF NOT EXISTS post (
  id serial PRIMARY KEY,
  title text,
  summary text,
  content text,
  url text,
  type text,
  published_at text,
  created_at timestamp,
  authors text, 
  downloadArticleLink text, --Para las páginas de articulos que permitan descargar el paper, aquí vá el link
  log_id integer references log(id) on update cascade on delete cascade,
  sourcename text
);

INSERT INTO source (id, name, url, type, active, created_at) VALUES (1, 'ArXiv CS', 'https://arxiv.org/list/cs/recent', 'paper', true, CURRENT_TIMESTAMP);


INSERT INTO source (id, name, url, type, active, created_at) VALUES (2, 'Revista Iberoamericana de Educación', 'https://rieoei.org/RIE/issue/archive', 'paper', true, CURRENT_TIMESTAMP);

INSERT INTO source (id, name, url, type, active, created_at) VALUES (3, 'MDPI', 'https://www.mdpi.com/rss?sort=pubdate&page_count=100&view=default', 'paper', true, CURRENT_TIMESTAMP);
