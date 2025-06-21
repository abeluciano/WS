
from collections import Counter

def get_trending_entities(articles, top_n=5):
    """
    Devuelve las 'top_n' entidades más mencionadas en el conjunto de artículos.
    """
    all_entities = []

    for article in articles:
        for ent_text, _ in article.entities:
            all_entities.append(ent_text)

    return Counter(all_entities).most_common(top_n)


def print_trending_entities(trending_list):
    print("\n📈 Entidades más mencionadas hoy:\n")
    for idx, (entity, count) in enumerate(trending_list, 1):
        print(f"{idx}. {entity} ({count} menciones)")
