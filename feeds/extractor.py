import feedparser
import spacy
from models.article import Article

nlp = spacy.load("es_core_news_md")

feeds = [
    "https://www.elcomercio.com/feed/",
    "https://larazon.pe/feed/",
    "https://elcomercio.pe/arc/outboundfeeds/rss/category/tecnologia/?outputType=xml",
    "https://elcomercio.pe/arc/outboundfeeds/rss/category/peru/?outputType=xml",
    "https://elcomercio.pe/arc/outboundfeeds/rss/category/economia/?outputType=xml",
    "https://elcomercio.pe/arc/outboundfeeds/rss/category/mundo/?outputType=xml",
    "https://elcomercio.pe/arc/outboundfeeds/rss/category/politica/?outputType=xml",
    "https://caretas.pe/feed/",
    "https://peru21.pe/rss/",
    "https://elbuho.pe/feed/",
    "https://elmen.pe/feed/",
    "https://diariouno.pe/feed/",
    "http://www.generaccion.com/noticia/rss/",
    "https://prensaregional.pe/feed/",
    "https://enlinea.pe/feed/",
    "https://diariodelcusco.pe/feed/",
    "https://proycontra.com.pe/feed/"
]

def extract_entities(text):
    doc = nlp(text)
    entities = set()
    for ent in doc.ents:
        if ent.label_ in ("PER", "ORG", "LOC"):
            entities.add((ent.text, ent.label_))
    return list(entities)

def extract_news():
    articles = []
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            title = entry.get("title", "")
            summary = entry.get("summary", "")
            published = entry.get("published", "")
            link = entry.get("link", "")
            author = entry.get("author", "Desconocido")

            content = f"{title}. {summary}"
            entities = extract_entities(content)

            article = Article(
                title=title,
                summary=summary,
                published=published,
                author=author,
                link=link,
                entities=entities
            )

            articles.append(article)
    return articles
