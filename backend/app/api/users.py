from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel

from app.database import get_db
from app.models.user import User
from app.services.auth import get_current_user

router = APIRouter()

class UserProfileResponse(BaseModel):
    id: str
    email: str
    full_name: str | None
    preferred_playback_speed: str

    class Config:
        from_attributes = True

class UpdatePreferencesRequest(BaseModel):
    preferred_playback_speed: str  # Ej: "1.0x", "1.5x", "2.0x", "3.0x"

@router.get("/me", response_model=UserProfileResponse)
async def get_my_profile(
    current_user_id: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Obtiene la información del usuario autenticado y sus ajustes de accesibilidad."""
    result = await db.execute(select(User).where(User.id == current_user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.patch("/me/preferences")
async def update_preferences(
    prefs: UpdatePreferencesRequest,
    current_user_id: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Actualiza las preferencias de aceleración de voz (1.0x - 3.0x)."""
    result = await db.execute(select(User).where(User.id == current_user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    user.preferred_playback_speed = prefs.preferred_playback_speed
    await db.commit()
    return {"message": "Preferencias de accesibilidad actualizadas con éxito"}