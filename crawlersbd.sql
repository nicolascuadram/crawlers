CREATE TABLE IF NOT EXISTS source (
  id integer PRIMARY KEY,
  name text,
  url text,
  type text,
  active boolean,
  created_at timestamp
);


CREATE TABLE IF NOT EXISTS log (
  id integer PRIMARY KEY,
  source_id integer references source(id) on delete cascade on update cascade,
  fetched_at timestamp,
  error_message text
);

CREATE TABLE IF NOT EXISTS post (
  id integer PRIMARY KEY,
  title text,
  summary text,
  content text,
  url text,
  type text,
  published_at timestamp,
  created_at timestamp,
  log_id integer references log(id) on update cascade on delete cascade,
  sourcename text
);

INSERT INTO source (id, name, url, type, active, created_at) VALUES
(1, 'TechCrunch', 'https://techcrunch.com', 'news', true, CURRENT_TIMESTAMP),
(2, 'ArXiv CS', 'https://arxiv.org/list/cs/recent', 'paper', true, CURRENT_TIMESTAMP),
(3, 'Medium AI', 'https://medium.com/tag/artificial-intelligence', 'blog', true, CURRENT_TIMESTAMP),
(4, 'IEEE Spectrum', 'https://spectrum.ieee.org', 'news', false, CURRENT_TIMESTAMP);

INSERT INTO log (id, source_id, fetched_at, error_message) VALUES
(1, 1, CURRENT_TIMESTAMP - interval '1 day', NULL),
(2, 2, CURRENT_TIMESTAMP - interval '12 hours', NULL),
(3, 3, CURRENT_TIMESTAMP - interval '6 hours', 'Timeout: scraping failed'),
(4, 4, CURRENT_TIMESTAMP - interval '2 days', NULL);

INSERT INTO post (id, title, summary, content, url, type, published_at, created_at, log_id, sourcename) VALUES
(1, 'OpenAI launches GPT-5', 'New version of GPT series released', 'Today, OpenAI released GPT-5...', 
 'https://techcrunch.com/gpt-5-launch', 'news', CURRENT_TIMESTAMP - interval '1 day', CURRENT_TIMESTAMP, 1, 'TechCrunch'),

(2, 'Transformer models revisited', 'Paper revisits attention mechanisms in large LMs', 
 'This paper explores improvements to Transformer architecture...', 
 'https://arxiv.org/abs/1234.5678', 'paper', CURRENT_TIMESTAMP - interval '2 days', CURRENT_TIMESTAMP, 2, 'ArXiv CS'),

(3, 'How AI is changing design', 'Blog article on AI-driven UI/UX trends', 
 'In this blog post, we explore how designers use AI...', 
 'https://medium.com/some-post', 'blog', CURRENT_TIMESTAMP - interval '3 days', CURRENT_TIMESTAMP, 1, 'Medium AI'),

(4, 'Quantum computing & AI', 'IEEE article on intersection of quantum and AI', 
 'As AI progresses, new frontiers in computing are explored...', 
 'https://spectrum.ieee.org/quantum-ai', 'news', CURRENT_TIMESTAMP - interval '4 days', CURRENT_TIMESTAMP, 4, 'IEEE Spectrum');


