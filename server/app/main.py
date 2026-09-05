from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configuración CORS para habilitar clientes web/móviles
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Bienvenido a la API de VocaLink",
        "status": "online",
        "accessibility_standard": "WCAG 2.1 AAA"
    }

# Incluir routers
# app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["Auth"])
# app.include_router(audio.router, prefix=f"{settings.API_V1_STR}/audio", tags=["Audio"])