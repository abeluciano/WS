from feeds.extractor import extract_news
from enrichment.enricher import enrich_entities
from rdf.rdf_builder import article_to_rdf, save_graph
from classification.classifier import classify_articles
from classification.grouper import group_articles_by_entity, print_groups
from classification.trending import get_trending_entities, print_trending_entities
from rdflib import Graph
import os

def main():
    print("🚀 Extrayendo noticias de RSS...")
    articles = extract_news()

    combined_graph = Graph()

    for idx, article in enumerate(articles):
        print(f"\n📰 Procesando artículo {idx + 1}: {article.title}")
        
        enriched = enrich_entities(article.entities)
        article.enriched_entities = enriched

        print("🔍 Entidades detectadas:")
        for ent, tipo in article.entities:
            print(f"   - {ent} ({tipo})")

        print("✨ Entidades enriquecidas:")
        for ent, data in enriched.items():
            print(f"   - {ent}:")
            for key, value in data.items():
                print(f"      {key}: {value}")

        graph = article_to_rdf(article)
        combined_graph += graph

    articles = classify_articles(articles)
    entity_groups = group_articles_by_entity(articles)
    print_groups(entity_groups)

    trending = get_trending_entities(articles)
    print_trending_entities(trending)

    os.makedirs("output", exist_ok=True)
    save_graph(combined_graph, "output/noticias_completas.ttl")

if __name__ == "__main__":
    main()
