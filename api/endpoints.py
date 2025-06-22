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
from concurrent.futures import ThreadPoolExecutor

# Se crea el router para agrupar las rutas de la API
router = APIRouter()

# Base de datos en memoria para almacenar artículos procesados
ARTICLES_DB = []


@router.get("/noticias")
def get_all_articles():
    """
    Retorna todos los artículos procesados almacenados en memoria.
    Cada artículo incluye información como título, resumen, fecha de publicación, entidades, etc.
    """
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


@router.get("/noticia/{article_id}")
def get_article(article_id: str):
    """
    Retorna un artículo específico a partir de su ID.
    Si no se encuentra el artículo, se devuelve un error.
    """
    for article in ARTICLES_DB:
        if article.id == article_id:
            return article.__dict__  # Devuelve el artículo como diccionario
    return {"error": "Artículo no encontrado"}


@router.get("/procesar")
def process_news():
    """
    Extrae noticias desde los feeds RSS, enriquece las entidades y clasifica cada artículo.
    El procesamiento se hace en paralelo usando ThreadPoolExecutor.
    Los artículos procesados se almacenan en ARTICLES_DB.
    """
    global ARTICLES_DB
    raw_articles = extract_news()

    def enrich_and_classify(article):
        # Asigna un ID único
        article.id = str(uuid.uuid4())
        # Enriquecimiento semántico de entidades
        article.enriched_entities = enrich_entities(article.entities)
        # Clasificación basada en palabras clave
        article.categories = classify_article(f"{article.title} {article.summary}")
        return article

    # Procesamiento en paralelo
    with ThreadPoolExecutor() as executor:
        enriched_articles = list(executor.map(enrich_and_classify, raw_articles))

    ARTICLES_DB = enriched_articles
    return {"mensaje": f"{len(ARTICLES_DB)} artículos procesados"}


@router.get("/clasificar")
def get_categories():
    """
    Devuelve una lista única de categorías detectadas en todos los artículos procesados.
    """
    categories = set()
    for article in ARTICLES_DB:
        if hasattr(article, "categories"):
            categories.update(article.categories)
    return {"categorias_detectadas": list(categories)}


@router.get("/grupos")
def get_entity_groups():
    """
    Agrupa artículos por entidades mencionadas.
    Devuelve un diccionario donde cada clave es una entidad y su valor es una lista de títulos de artículos que la mencionan.
    """
    groups = group_articles_by_entity(ARTICLES_DB)
    result = {}
    for entity, articles in groups.items():
        result[entity] = [article.title for article in articles]
    return result


@router.get("/trending")
def get_trending():
    """
    Retorna las entidades más mencionadas entre los artículos procesados (Top 10).
    """
    trending = get_trending_entities(ARTICLES_DB)
    return {"entidades_mas_mencionadas": trending[:10]}  # top 10
