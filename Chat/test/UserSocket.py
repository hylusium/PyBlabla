import asyncio
import websockets

# Fonction pour envoyer des messages au serveur
async def send_messages(websocket):
    while True:
        message = input("Entrez votre message à envoyer : ")
        await websocket.send(message)
        print(f"Message envoyé : {message}")

# Fonction pour recevoir les messages du serveur
async def receive_messages(websocket):
    while True:
        response = await websocket.recv()
        print(f"Réponse du serveur : {response}")

# Fonction principale
async def communicate():
    uri = "ws://90.5.227.209:8765"
    async with websockets.connect(uri) as websocket:
        # Exécuter simultanément l'envoi et la réception des messages
        await asyncio.gather(
            send_messages(websocket),
            receive_messages(websocket)
        )

# Lancer l'application
asyncio.run(communicate())
