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
    Retorna una lista de categorías para el artículo, basado en keywords.
    """
    text = article_text.lower()
    assigned_categories = []

    for category, keywords in CATEGORIES.items():
        if any(keyword in text for keyword in keywords):
            assigned_categories.append(category)

    return assigned_categories or ["sin categoría"]


def classify_articles(articles):
    """
    Agrega las categorías detectadas a cada artículo.
    """
    for article in articles:
        combined_text = f"{article.title} {article.summary}"
        categories = classify_article(combined_text)
        article.categories = categories
        print(f"📌 Categorías para '{article.title}': {categories}")
    return articles
