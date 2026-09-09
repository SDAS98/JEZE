from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.api import rooms
from app.config import settings
from app.api import auth, audio
from live_engine.manager import room_manager
from app.api import auth, audio, rooms, users


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir archivos de audio locales
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir Routers de la API
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["Autenticación"])
app.include_router(audio.router, prefix=f"{settings.API_V1_STR}/audio", tags=["Audio y A11y"])
app.include_router(rooms.router, prefix=f"{settings.API_V1_STR}/live", tags=["Live Audio Rooms"])
app.include_router(users.router, prefix=f"{settings.API_V1_STR}/users", tags=["Usuarios y Accesibilidad"])

@app.get("/")
async def root():
    return {
        "message": "Bienvenido a la API de JEZE",
        "status": "online",
        "accessibility_standard": "WCAG 2.1 AAA"
    }