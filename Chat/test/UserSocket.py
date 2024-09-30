import asyncio
import websockets

async def hello():
    uri = "ws://90.5.227.209:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Bonjour, julio!")
        response = await websocket.recv()
        print(f"Réponse du serveur: {response}")

# Lancer le client WebSocket
asyncio.run(hello())
