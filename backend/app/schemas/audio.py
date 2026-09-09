from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.audio import AudioFormat, AudioStatus

class AudioUploadResponse(BaseModel):
    id: str
    file_url: str
    format: AudioFormat
    duration_seconds: float
    status: AudioStatus
    message: str

class AudioDetail(BaseModel):
    id: str
    user_id: str
    file_url: str
    format: AudioFormat
    duration_seconds: float
    status: AudioStatus
    transcript: Optional[str] = None
    language: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True