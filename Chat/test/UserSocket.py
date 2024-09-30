
import asyncio
import websockets

async def send_message():
    uri = "ws://90.5.227.209:8765"
    async with websockets.connect(uri) as websocket:
<<<<<<< HEAD
        await websocket.send("Bonjour, Hugo, je te bouffe le cul!")
        response = await websocket.recv()
        print(f"Réponse du serveur: {response}")
=======
        # Envoyer un message au serveur
        message = input("entrer votre message a envoyer : ")
        await websocket.send(message)
        print(f"Message envoyé : {message}")
>>>>>>> f6ef836b2026c39e36ebce10c81a0daa2264e003

        # Recevoir la réponse du serveur
        response = await websocket.recv()
        print(f"Réponse du serveur : {response}")

# Lancer le client
asyncio.run(send_message())
