import feedparser
import spacy
from models.article import Article

# Carga el modelo de procesamiento de lenguaje natural en español de spaCy
nlp = spacy.load("es_core_news_md")

# Lista de fuentes RSS que serán procesadas
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
    """
    Extrae entidades nombradas (persona, organización, lugar) del texto.

    Args:
        text (str): Texto de entrada (ej: título + resumen de noticia).

    Returns:
        list: Lista de tuplas con entidades detectadas, como (nombre, tipo).
    """
    doc = nlp(text)
    entities = set()

    for ent in doc.ents:
        # Filtramos solo personas (PER), organizaciones (ORG) y lugares (LOC)
        if ent.label_ in ("PER", "ORG", "LOC"):
            entities.add((ent.text, ent.label_))

    return list(entities)

def extract_news():
    """
    Procesa todas las fuentes RSS, extrae noticias y sus entidades nombradas.

    Returns:
        list: Lista de objetos Article con los datos estructurados.
    """
    articles = []

    # Iteramos por cada URL RSS definida en `feeds`
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)  # Parseamos el RSS

        for entry in feed.entries:
            # Extraemos campos básicos
            title = entry.get("title", "")
            summary = entry.get("summary", "")
            published = entry.get("published", "")
            link = entry.get("link", "")
            author = entry.get("author", "Desconocido")

            # Combinamos título y resumen para analizar entidades
            content = f"{title}. {summary}"
            entities = extract_entities(content)

            # Creamos un objeto Article con los datos extraídos
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
