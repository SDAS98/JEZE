import os
import aiofiles
from fastapi import UploadFile, HTTPException

UPLOAD_DIR = "static/audio"

os.makedirs(UPLOAD_DIR, exist_ok=True)

async def upload_audio_to_s3(file: UploadFile) -> str:
    """
    En desarrollo guarda el archivo localmente en /static/audio.
    En producción se puede reemplazar por subida a AWS S3 / Cloudflare R2 con boto3.
    """
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        async with aiofiles.open(file_path, 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)
        
        return f"/static/audio/{file.filename}"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error guardando archivo de audio: {str(e)}")