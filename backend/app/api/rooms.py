from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status
from live_engine.manager import room_manager

router = APIRouter()

@router.websocket("/ws/room/{room_id}")
async def live_audio_room_endpoint(websocket: WebSocket, room_id: str):
    await room_manager.connect(room_id, websocket)
    try:
        while True:
            # Recibe eventos de señalización (SDP offers/answers, ICE candidates)
            data = await websocket.receive_json()
            await room_manager.broadcast(room_id, data, sender=websocket)
    except WebSocketDisconnect:
        room_manager.disconnect(room_id, websocket)
        await room_manager.broadcast(
            room_id, 
            {"event": "user_disconnected", "message": "Un participante abandonó la sala"}, 
            sender=websocket
        )