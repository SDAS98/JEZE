from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.database import get_db
from app.models.audio import AudioPost
from app.schemas.audio import AudioDetail
from fastapi import APIRouter

router = APIRouter()

# (Se mantiene el endpoint /upload anterior...)

@router.get("/feed", response_model=List[AudioDetail])
async def get_audio_feed(
    skip: int = 0, 
    limit: int = 20, 
    db: AsyncSession = Depends(get_db)
):
    """Obtiene el feed de notas de voz procesadas para el cliente accesible."""
    result = await db.execute(
        select(AudioPost)
        .order_by(AudioPost.created_at.desc())
        .offset(skip)
        .limit(limit)
    )
    audios = result.scalars().all()
    return audios

@router.get("/{audio_id}", response_model=AudioDetail)
async def get_audio_by_id(
    audio_id: str, 
    db: AsyncSession = Depends(get_db)
):
    """Consulta los metadatos y transcripción de un audio específico."""
    result = await db.execute(select(AudioPost).where(AudioPost.id == audio_id))
    audio = result.scalar_one_or_none()
    
    if not audio:
        raise HTTPException(status_code=404, detail="Audio no encontrado")
        
    return audio