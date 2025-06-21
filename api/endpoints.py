# api/endpoints.py
from fastapi import APIRouter
from models.article import Article
from feeds.extractor import extract_news
from enrichment.enricher import enrich_entities
from classification.classifier import classify_article
from classification.grouper import group_articles_by_entity
from classification.trending import get_trending_entities

from typing import List
import uuid

router = APIRouter()


ARTICLES_DB = []

@router.get("/noticias")
def get_all_articles():
    return [
        {
            "id": article.id,
            "title": article.title,
            "summary": article.summary,
            "published": article.published,
            "author": article.author,
            "link": article.link,
            "entities": article.entities,
            "enriched_entities": article.enriched_entities,
            "category": getattr(article, "category", "sin categoría")
        }
        for article in ARTICLES_DB
    ]


# api/endpoints.py
@router.get("/noticia/{article_id}")
def get_article(article_id: str):
    for article in ARTICLES_DB:
        if article.id == article_id:
            return article.__dict__  # <- aquí el cambio
    return {"error": "Artículo no encontrado"}


from concurrent.futures import ThreadPoolExecutor
import uuid

@router.get("/procesar")
def process_news():
    global ARTICLES_DB
    raw_articles = extract_news()

    def enrich_and_classify(article):
        article.id = str(uuid.uuid4())
        article.enriched_entities = enrich_entities(article.entities)
        # Clasificación también aquí, para mantenerlo paralelo
        article.categories = classify_article(f"{article.title} {article.summary}")
        return article

    with ThreadPoolExecutor() as executor:
        enriched_articles = list(executor.map(enrich_and_classify, raw_articles))

    ARTICLES_DB = enriched_articles
    return {"mensaje": f"{len(ARTICLES_DB)} artículos procesados"}


@router.get("/clasificar")
def get_categories():
    categories = set()
    for article in ARTICLES_DB:
        if hasattr(article, "categories"):
            categories.update(article.categories)
    return {"categorias_detectadas": list(categories)}


# NUEVO: /grupos
@router.get("/grupos")
def get_entity_groups():
    groups = group_articles_by_entity(ARTICLES_DB)
    result = {}
    for entity, articles in groups.items():
        result[entity] = [article.title for article in articles]
    return result

# NUEVO: /trending
@router.get("/trending")
def get_trending():
    trending = get_trending_entities(ARTICLES_DB)
    return {"entidades_mas_mencionadas": trending[:10]}  # top 10
