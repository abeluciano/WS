from collections import defaultdict

def group_articles_by_entity(articles):
    """
    Agrupa artículos por entidades nombradas (personas, lugares, organizaciones, etc.).

    Args:
        articles (list): Lista de artículos, donde cada artículo debe contener un atributo `entities`,
                         el cual es una lista de tuplas (entidad, tipo_entidad).

    Returns:
        dict: Un diccionario donde cada clave es el texto de una entidad (str) y
              el valor es una lista de artículos que mencionan dicha entidad.
    """
    # Diccionario con listas por defecto para almacenar artículos por entidad
    entity_groups = defaultdict(list)

    # Recorremos todos los artículos
    for article in articles:
        # Para cada entidad mencionada en el artículo
        for ent_text, ent_type in article.entities:
            # Agregamos el artículo bajo la clave de la entidad
            entity_groups[ent_text].append(article)

    return entity_groups


def print_groups(entity_groups, min_articles=2):
    """
    Imprime por consola los grupos de entidades mencionadas en múltiples artículos.

    Args:
        entity_groups (dict): Diccionario con entidades como claves y listas de artículos como valores.
        min_articles (int): Umbral mínimo de artículos por entidad para ser impresa (por defecto 2).
    """
    print("\n🔗 Agrupación de noticias relacionadas por entidad:\n")

    # Iteramos sobre cada entidad y los artículos donde aparece
    for entity, related_articles in entity_groups.items():
        if len(related_articles) >= min_articles:
            # Imprimimos entidad y cantidad de apariciones
            print(f"🧠 {entity} ({len(related_articles)} noticias):")
            for art in related_articles:
                print(f"   - {art.title}")
            print("-" * 50)
