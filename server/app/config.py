from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "VocaLink API"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # Seguridad
    SECRET_KEY: str = "CAMBIAR_POR_UNA_CLAVE_SECRETA_SEGURA"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 días
    
    # Base de datos
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost:5432/vocalink_db"

    class Config:
        env_file = ".env"

settings = Settings()