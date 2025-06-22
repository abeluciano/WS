# Importa la clase FastAPI para crear la aplicación web
from fastapi import FastAPI

# Importa el router que contiene todos los endpoints definidos en tu módulo de API
from api.endpoints import router

# Crea una instancia de la aplicación FastAPI
# El título personalizado aparecerá en la documentación interactiva (Swagger UI)
app = FastAPI(title="📰 API de Noticias Enriquecidas")

# Se incluye el router con todas las rutas definidas en `api/endpoints.py`
# Esto permite una estructura modular y limpia para mantener organizadas las rutas
app.include_router(router)
