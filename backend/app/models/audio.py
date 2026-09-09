import enum
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.models.user import Base  # Asumiendo Base = declarative_base()

class AudioFormat(str, enum.Enum):
    OPUS = "opus"
    AAC = "aac"
    MP3 = "mp3"

class AudioStatus(str, enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    READY = "ready"
    FAILED = "failed"

class AudioPost(Base):
    __tablename__ = "audio_posts"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    
    file_url = Column(String, nullable=False)
    format = Column(Enum(AudioFormat), default=AudioFormat.OPUS, nullable=False)
    duration_seconds = Column(Float, nullable=False)
    status = Column(Enum(AudioStatus), default=AudioStatus.PENDING, nullable=False)
    
    # Accesibilidad (Speech-to-Text)
    transcript = Column(Text, nullable=True)
    language = Column(String, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)