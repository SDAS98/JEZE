import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "JEZE API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Seguridad y Autenticación
    SECRET_KEY: str = os.getenv("SECRET_KEY", "SUPER_SECRET_KEY_JEZE_CHANGE_IN_PROD")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 días
    
    # Base de Datos (soporta PostgreSQL por defecto, cae en SQLite asíncrono para dev)
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "sqlite+aiosqlite:///./jeze.db"
    )

    class Config:
        case_sensitive = True

settings = Settings()