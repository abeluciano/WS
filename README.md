# 📰 Backend - Agregador y Clasificador de Noticias

Este backend implementa una **API de noticias inteligente** que:

- Extrae artículos desde múltiples *feeds RSS* de medios peruanos.
- Enriquece semánticamente las entidades mencionadas (personas, lugares, organizaciones) usando **Wikidata**.
- Clasifica automáticamente las noticias en categorías como *política*, *economía*, *sociedad*, entre otras.
- Agrupa noticias relacionadas por entidades comunes.
- Detecta temas *trending* en tiempo real.

---

## ⚙️ Tecnologías utilizadas

- **Python 3.10+**
- **FastAPI** (API REST)
- **feedparser** (extracción RSS)
- **SPARQLWrapper** (consultas a Wikidata)
- **ThreadPoolExecutor** (procesamiento paralelo)
- **Uvicorn** (servidor ASGI)

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/backend-noticias.git
cd backend-noticias
````

### 2. Crear y activar un entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si no existe `requirements.txt`, puedes generarlo con:

```bash
pip freeze > requirements.txt
```

### 4. Ejecutar el servidor

```bash
uvicorn main:app --reload
```

Esto iniciará el servidor en `http://127.0.0.1:8000`.

---

## 📡 Endpoints principales

| Endpoint        | Método | Descripción                            |
| --------------- | ------ | -------------------------------------- |
| `/procesar`     | GET    | Extrae, enriquece y clasifica noticias |
| `/noticias`     | GET    | Retorna todas las noticias procesadas  |
| `/noticia/{id}` | GET    | Retorna una noticia por su ID          |
| `/clasificar`   | GET    | Lista las categorías detectadas        |
| `/grupos`       | GET    | Agrupa noticias por entidades comunes  |
| `/trending`     | GET    | Muestra las entidades más mencionadas  |

---

## 📰 Fuentes RSS utilizadas

* [https://www.elcomercio.com/feed/](https://www.elcomercio.com/feed/)
* [https://larazon.pe/feed/](https://larazon.pe/feed/)
* [https://elcomercio.pe/arc/outboundfeeds/rss/category/tecnologia/?outputType=xml](https://elcomercio.pe/arc/outboundfeeds/rss/category/tecnologia/?outputType=xml)
* [https://elcomercio.pe/arc/outboundfeeds/rss/category/peru/?outputType=xml](https://elcomercio.pe/arc/outboundfeeds/rss/category/peru/?outputType=xml)
* [https://elcomercio.pe/arc/outboundfeeds/rss/category/economia/?outputType=xml](https://elcomercio.pe/arc/outboundfeeds/rss/category/economia/?outputType=xml)
* [https://elcomercio.pe/arc/outboundfeeds/rss/category/mundo/?outputType=xml](https://elcomercio.pe/arc/outboundfeeds/rss/category/mundo/?outputType=xml)
* [https://elcomercio.pe/arc/outboundfeeds/rss/category/politica/?outputType=xml](https://elcomercio.pe/arc/outboundfeeds/rss/category/politica/?outputType=xml)
* [https://caretas.pe/feed/](https://caretas.pe/feed/)
* [https://peru21.pe/rss/](https://peru21.pe/rss/)
* [https://elbuho.pe/feed/](https://elbuho.pe/feed/)
* [https://elmen.pe/feed/](https://elmen.pe/feed/)
* [https://diariouno.pe/feed/](https://diariouno.pe/feed/)
* [http://www.generaccion.com/noticia/rss/](http://www.generaccion.com/noticia/rss/)
* [https://prensaregional.pe/feed/](https://prensaregional.pe/feed/)
* [https://enlinea.pe/feed/](https://enlinea.pe/feed/)
* [https://diariodelcusco.pe/feed/](https://diariodelcusco.pe/feed/)
* [https://proycontra.com.pe/feed/](https://proycontra.com.pe/feed/)

---

## 📁 Estructura del proyecto

```
.
├── api/
│   └── endpoints.py         # Rutas de la API
├── classification/
│   ├── classifier.py        # Clasificación de artículos
│   ├── grouper.py           # Agrupamiento por entidad
│   └── trending.py          # Detección de temas trending
├── enrichment/
│   └── enricher.py          # Enriquecimiento desde Wikidata
├── feeds/
│   └── extractor.py         # Extracción desde feeds RSS
├── models/
│   └── article.py           # Modelo de artículo
├── main.py                  # Punto de entrada de FastAPI
└── requirements.txt         # Dependencias del proyecto
```

---

## ✅ Estado actual

* [x] Extracción desde más de 15 feeds RSS.
* [x] Procesamiento en paralelo.
* [x] Enriquecimiento semántico.
* [x] Clasificación automática.
* [x] Agrupamiento y trending.
* [x] Documentación de la API disponible vía Swagger (`/docs`).
