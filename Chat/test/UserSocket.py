
import asyncio
import websockets

async def send_message():
    uri = "ws://90.5.227.209:8765"
    async with websockets.connect(uri) as websocket:
        # Envoyer un message au serveur
        message = "Salut, serveur !"
        await websocket.send(message)
        print(f"Message envoyé : {message}")

        # Recevoir la réponse du serveur
        response = await websocket.recv()
        print(f"Réponse du serveur : {response}")

# Lancer le client
asyncio.run(send_message())
