from fastapi import FastAPI
from api.endpoints import router

app = FastAPI(title="📰 API de Noticias Enriquecidas")
app.include_router(router)
