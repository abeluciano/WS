from collections import defaultdict

def group_articles_by_entity(articles):
    """
    Devuelve un diccionario donde cada entidad es clave,
    y su valor es la lista de artículos que la mencionan.
    """
    entity_groups = defaultdict(list)

    for article in articles:
        for ent_text, ent_type in article.entities:
            entity_groups[ent_text].append(article)

    return entity_groups


def print_groups(entity_groups, min_articles=2):
    """
    Imprime entidades que aparecen en al menos 'min_articles' diferentes.
    """
    print("\n🔗 Agrupación de noticias relacionadas por entidad:\n")
    for entity, related_articles in entity_groups.items():
        if len(related_articles) >= min_articles:
            print(f"🧠 {entity} ({len(related_articles)} noticias):")
            for art in related_articles:
                print(f"   - {art.title}")
            print("-" * 50)
