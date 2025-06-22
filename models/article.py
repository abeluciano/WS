from dataclasses import dataclass, field
from typing import List, Tuple, Dict

@dataclass
class Article:
    """
    Representa una noticia con su contenido y metadatos extraídos.

    Atributos:
        title (str): Título del artículo.
        summary (str): Resumen o descripción breve.
        published (str): Fecha de publicación.
        author (str): Autor o fuente de la noticia.
        link (str): URL del artículo original.
        entities (List[Tuple[str, str]]): Entidades nombradas detectadas,
            como una lista de tuplas (nombre, tipo).
        enriched_entities (Dict): Información adicional de entidades
            enriquecidas, por ejemplo desde DBpedia.
        id (str): Identificador único (opcional, puede usarse UUID).
    """
    
    title: str
    summary: str
    published: str
    author: str
    link: str
    entities: List[Tuple[str, str]]  # Lista de entidades detectadas (texto, tipo)
    enriched_entities: Dict = field(default_factory=dict)  # Datos enriquecidos por entidad
    id: str = ""  # Se puede asignar un UUID más adelante si es necesario
