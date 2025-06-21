from dataclasses import dataclass, field
from typing import List, Tuple, Dict

@dataclass
class Article:
    title: str
    summary: str
    published: str
    author: str
    link: str
    entities: List[Tuple[str, str]]
    enriched_entities: Dict = field(default_factory=dict)
    id: str = ""  # si quieres usar UUID después
