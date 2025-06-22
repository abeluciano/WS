# Importa FastAPI para crear la app web
from fastapi import FastAPI

# Importa el middleware de CORS
from fastapi.middleware.cors import CORSMiddleware

# Importa el router de rutas definidas en tu módulo
from api.endpoints import router

# Crea la instancia de FastAPI con título personalizado (aparece en Swagger UI)
app = FastAPI(title="📰 API de Noticias Enriquecidas")

# Habilita CORS para permitir solicitudes desde cualquier origen
# Esto es necesario si el frontend está en un dominio diferente (como localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Permite solicitudes desde cualquier dominio
    allow_credentials=True,     # Permite el uso de cookies/autenticación (si aplica)
    allow_methods=["*"],        # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],        # Permite cualquier encabezado
)

# Registra las rutas importadas desde el router
app.include_router(router)
