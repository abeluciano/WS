from collections import Counter

def get_trending_entities(articles, top_n=5):
    """
    Extrae las entidades más mencionadas en una lista de artículos.

    Args:
        articles (list): Lista de artículos, cada uno con una propiedad `entities`,
                         la cual es una lista de tuplas (entidad, tipo).
        top_n (int): Número de entidades más frecuentes a devolver (por defecto 5).

    Returns:
        list: Lista de tuplas (entidad, conteo) ordenadas de mayor a menor frecuencia.
    """
    all_entities = []

    # Reunimos todas las entidades mencionadas en los artículos
    for article in articles:
        for ent_text, _ in article.entities:
            all_entities.append(ent_text)

    # Contamos la frecuencia de cada entidad y retornamos las top_n más comunes
    return Counter(all_entities).most_common(top_n)


def print_trending_entities(trending_list):
    """
    Imprime en consola el ranking de entidades más mencionadas.

    Args:
        trending_list (list): Lista de tuplas (entidad, conteo) como las devueltas por get_trending_entities.
    """
    print("\n📈 Entidades más mencionadas hoy:\n")

    for idx, (entity, count) in enumerate(trending_list, 1):
        print(f"{idx}. {entity} ({count} menciones)")
