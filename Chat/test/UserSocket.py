import asyncio
import websockets

async def hello():
    uri = "ws://192.168.1.34:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Bonjour, julio!")
        response = await websocket.recv()
        print(f"Réponse du serveur: {response}")

# Lancer le client WebSocket
asyncio.run(hello())
