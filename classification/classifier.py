# Diccionario que mapea categorías temáticas a una lista de palabras clave asociadas.
CATEGORIES = {
    "política": [
        "congreso", "presidente", "elecciones", "gobierno",
        "ministro", "política", "estado", "partido político"
    ],
    "economía": [
        "inflación", "banco", "mercado", "dólar", "exportación",
        "economía", "sunat", "ingresos", "impuestos"
    ],
    "deportes": [
        "fútbol", "liga", "gol", "partido", "selección",
        "campeonato", "deportes", "jugador", "club"
    ],
    "tecnología": [
        "inteligencia artificial", "google", "app", "software",
        "startup", "tecnología", "innovación", "smartphone", "internet"
    ],
    "mundo": [
        "eeuu", "ucrania", "china", "internacional", "conflicto",
        "guerra", "rusia", "mundo", "israel", "otan"
    ],
    "sociedad": [
        "ciudadanos", "protesta", "salud", "educación", "crimen",
        "accidente", "sociedad", "familia", "niños", "hospital"
    ]
}


def classify_article(article_text):
    """
    Clasifica un artículo en una o más categorías basadas en la aparición de keywords.
    
    Args:
        article_text (str): Texto del artículo (puede ser título, resumen, etc.).
        
    Returns:
        list: Lista de categorías detectadas, o ['sin categoría'] si no se encontró coincidencia.
    """
    # Convierte todo el texto a minúsculas para hacer la búsqueda insensible a mayúsculas
    text = article_text.lower()
    assigned_categories = []

    # Recorre todas las categorías y verifica si alguna palabra clave aparece en el texto
    for category, keywords in CATEGORIES.items():
        if any(keyword in text for keyword in keywords):
            assigned_categories.append(category)

    # Devuelve al menos una categoría (por defecto "sin categoría" si no hay coincidencias)
    return assigned_categories or ["sin categoría"]


def classify_articles(articles):
    """
    Clasifica una lista de artículos, agregando las categorías detectadas a cada uno.
    
    Args:
        articles (list): Lista de objetos artículo con atributos `title` y `summary`.
    
    Returns:
        list: Misma lista de artículos, ahora con un nuevo atributo `categories`.
    """
    for article in articles:
        # Une título y resumen para tener más contexto en la clasificación
        combined_text = f"{article.title} {article.summary}"
        
        # Aplica clasificación por palabras clave
        categories = classify_article(combined_text)
        
        # Agrega las categorías detectadas al objeto artículo
        article.categories = categories
        
        # Imprime log para debug
        print(f"📌 Categorías para '{article.title}': {categories}")
    
    return articles
