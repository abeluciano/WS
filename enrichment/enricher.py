from SPARQLWrapper import SPARQLWrapper, JSON

# Endpoint de DBpedia
DBPEDIA_ENDPOINT = "https://dbpedia.org/sparql"

def build_sparql_query(entity_label: str) -> str:
    """
    Devuelve una consulta SPARQL para una entidad con label en español.
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
    Ejecuta una consulta SPARQL y devuelve los datos como dict.
    """
    sparql = SPARQLWrapper(DBPEDIA_ENDPOINT)
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(JSON)

    try:
        results = sparql.query().convert()
        bindings = results["results"]["bindings"]
        if not bindings:
            return {}
        
        result = bindings[0]
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
    Para una lista de entidades [(nombre, tipo)], devuelve un dict enriquecido por nombre.
    """
    enriched = {}
    for entity_name, _ in entities:
        query = build_sparql_query(entity_name)
        data = query_dbpedia(query)
        if data:
            enriched[entity_name] = data
    return enriched
