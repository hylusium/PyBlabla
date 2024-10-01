
import asyncio
import websockets

# Fonction pour envoyer des messages au serveur
async def send_messages(websocket):
    while True:
        # Utiliser asyncio pour capturer l'entrée utilisateur sans bloquer
        message = await asyncio.to_thread(input, "Entrez votre message à envoyer : ")
        await websocket.send(message)
        print(f"Message envoyé : {message}")

# Fonction pour recevoir des messages du serveur
async def receive_messages(websocket):
    while True:
        try:
            response = await websocket.recv()
            print(f"Message reçu du serveur : {response}")
        except websockets.ConnectionClosed:
            print("Connexion fermée par le serveur.")
            break

# Fonction pour gérer la communication client-serveur
async def communicate():
    uri = "ws://90.5.227.209:8765"
    try:
        async with websockets.connect(uri) as websocket:
            # Lancer l'envoi et la réception simultanément
            send_task = asyncio.create_task(send_messages(websocket))
            receive_task = asyncio.create_task(receive_messages(websocket))

            # Attendre que l'une des tâches se termine (en cas d'erreur ou de déconnexion)
            await asyncio.gather(send_task, receive_task)
    except Exception as e:
        print(f"Erreur de connexion : {e}")

asyncio.run(communicate())
