from fastapi import FastAPI, WebSocket
from model import predict

app = FastAPI()

@app.websocket("/ws")
async def digit_socket(websocket: WebSocket):
    await websocket.accept()
    while True:
        image_data = await websocket.receive_bytes()
        result = predict(image_data)
        await websocket.send_json(result)