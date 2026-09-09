import whisper
import logging
from app.models.audio import AudioStatus

logger = logging.getLogger(__name__)

# Carga del modelo (se puede ajustar a 'tiny', 'base', 'small' o 'medium' según recursos)
whisper_model = whisper.load_model("base")

async def process_audio_transcription(audio_id: str, file_url: str):
    """
    Tarea en segundo plano para descargar/procesar audio y generar la transcripción.
    """
    try:
        logger.info(f"Iniciando transcripción para audio_id: {audio_id}")
        
        # 1. Transcribir el audio mediante el motor Whisper
        result = whisper_model.transcribe(file_url)
        
        extracted_text = result.get("text", "").strip()
        detected_language = result.get("language", "es")
        
        # 2. Actualizar la base de datos con el texto accesible
        # await update_audio_record(
        #     audio_id=audio_id,
        #     transcript=extracted_text,
        #     language=detected_language,
        #     status=AudioStatus.READY
        # )
        logger.info(f"Transcripción completada con éxito para {audio_id}: {extracted_text[:50]}...")

    except Exception as e:
        logger.error(f"Error procesando transcripción de audio {audio_id}: {str(e)}")
        # await update_audio_record(audio_id=audio_id, status=AudioStatus.FAILED)