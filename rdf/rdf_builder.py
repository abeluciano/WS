from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, FOAF, DC
from models.article import Article
import hashlib

# Namespace base para tus recursos locales
EX = Namespace("http://example.org/noticias#")
DBPEDIA = Namespace("http://dbpedia.org/resource/")
DBO = Namespace("http://dbpedia.org/ontology/")

def hash_uri(value: str) -> str:
    """
    Crea un URI único a partir de un string (usando hash)
    """
    return hashlib.md5(value.encode()).hexdigest()

def article_to_rdf(article: Article) -> Graph:
    g = Graph()
    
    # Bind namespaces
    g.bind("ex", EX)
    g.bind("foaf", FOAF)
    g.bind("dc", DC)
    g.bind("dbo", DBO)

    # Crear URI única para el artículo
    article_id = hash_uri(article.title + article.published)
    article_uri = EX[f"article_{article_id}"]

    # Tripletas del artículo
    g.add((article_uri, RDF.type, EX.NewsArticle))
    g.add((article_uri, DC.title, Literal(article.title)))
    g.add((article_uri, DC.description, Literal(article.summary)))
    g.add((article_uri, DC.date, Literal(article.published)))
    g.add((article_uri, DC.creator, Literal(article.author)))
    g.add((article_uri, FOAF.page, URIRef(article.link)))

    # Entidades detectadas y enriquecidas
    for entity_name, entity_type in article.entities:
        entity_uri = URIRef(DBPEDIA[entity_name.replace(" ", "_")])

        # Relacionar con artículo
        g.add((article_uri, EX.mentions, entity_uri))

        # Si hay enriquecimiento, agregarlo
        enriched = article.enriched_entities.get(entity_name)
        if enriched:
            g.add((entity_uri, RDF.type, DBO[entity_type.lower()]))
            if enriched.get("birthDate"):
                g.add((entity_uri, DBO.birthDate, Literal(enriched["birthDate"])))
            if enriched.get("occupation"):
                g.add((entity_uri, DBO.occupation, URIRef(enriched["occupation"])))
            if enriched.get("description"):
                g.add((entity_uri, RDFS.comment, Literal(enriched["description"], lang="es")))

    return g

def save_graph(graph: Graph, filename: str):
    """
    Guarda el grafo RDF en formato Turtle
    """
    graph.serialize(destination=filename, format="turtle")
    print(f"✅ Grafo guardado como {filename}")
