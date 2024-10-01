import asyncio
import websockets

async def send_messages(websocket):
    while True:
        message = await asyncio.to_thread(input, "Entrez votre message à envoyer : ")
        await websocket.send(message)
        print(f"Message envoyé : {message}")

async def receive_messages(websocket):
    while True:
        try:
            response = await websocket.recv()
            print(f"Message reçu du serveur : {response}")
        except websockets.ConnectionClosed:
            print("Connexion fermée par le serveur.")
            break

async def communicate():
    uri = "ws://90.5.227.209:8765"
    try:
        async with websockets.connect(uri) as websocket:
            send_task = asyncio.create_task(send_messages(websocket))
            receive_task = asyncio.create_task(receive_messages(websocket))

            await asyncio.gather(send_task, receive_task)
    except Exception as e:
        print(f"Erreur de connexion : {e}")

asyncio.run(communicate())
