from SPARQLWrapper import SPARQLWrapper, JSON

# URL del endpoint público de DBpedia para consultas SPARQL
DBPEDIA_ENDPOINT = "https://dbpedia.org/sparql"

def build_sparql_query(entity_label: str) -> str:
    """
    Construye una consulta SPARQL para buscar información sobre una entidad específica.

    Args:
        entity_label (str): Nombre de la entidad en español.

    Returns:
        str: Consulta SPARQL que busca información básica (fecha de nacimiento, ocupación y descripción).
    """
    return f"""
    SELECT ?person ?birthDate ?occupation ?description WHERE {{
        ?person rdfs:label "{entity_label}"@es ;
                dbo:birthDate ?birthDate ;
                dbo:occupation ?occupation ;
                rdfs:comment ?description .
        FILTER(LANG(?description) = "es")
    }}
    LIMIT 1
    """

def query_dbpedia(sparql_query: str) -> dict:
    """
    Ejecuta una consulta SPARQL en DBpedia y devuelve los resultados estructurados.

    Args:
        sparql_query (str): Consulta SPARQL válida.

    Returns:
        dict: Diccionario con URI, fecha de nacimiento, ocupación y descripción. 
              Si no hay resultados, devuelve un diccionario vacío.
    """
    sparql = SPARQLWrapper(DBPEDIA_ENDPOINT)
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(JSON)

    try:
        results = sparql.query().convert()
        bindings = results["results"]["bindings"]
        if not bindings:
            return {}  # No se encontró información

        result = bindings[0]  # Solo usamos el primer resultado
        return {
            "uri": result["person"]["value"],
            "birthDate": result.get("birthDate", {}).get("value"),
            "occupation": result.get("occupation", {}).get("value"),
            "description": result.get("description", {}).get("value")
        }
    except Exception as e:
        print(f"⚠️ Error al consultar DBpedia: {e}")
        return {}

def enrich_entities(entities: list) -> dict:
    """
    Enriquecer una lista de entidades con información externa desde DBpedia.

    Args:
        entities (list): Lista de tuplas (nombre, tipo), típicamente extraídas de artículos.

    Returns:
        dict: Diccionario con el nombre de la entidad como clave y la información enriquecida como valor.
    """
    enriched = {}

    # Iteramos sobre cada entidad para construir la consulta y obtener los datos
    for entity_name, _ in entities:
        query = build_sparql_query(entity_name)
        data = query_dbpedia(query)
        if data:
            enriched[entity_name] = data  # Solo agregamos si hay resultados

    return enriched
