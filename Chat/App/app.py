import customtkinter as ctk
import asyncio
import websockets
import threading

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Chat Python")
root.geometry("400x400")

nomUtilisateur = "test"
websocket = None
messageUser = None

# Function to send messages asynchronously
async def send_messages():
    global websocket, messageUser
    if websocket and messageUser:
        message = f"{nomUtilisateur}: {messageUser}\n"
        await websocket.send(message)
        print(f"Message envoyé : {message}")

# Function to receive messages from the websocket
async def receive_messages():
    global websocket
    while True:
        try:
            response = await websocket.recv()
            print(f"Message reçu du serveur : {response}")
            chatBox.configure(state="normal")
            chatBox.insert(ctk.END, f"{response}\n")
            chatBox.configure(state="disabled")
        except websockets.ConnectionClosed:
            print("Connexion fermée par le serveur.")
            break

# Function to establish communication with the websocket server
async def communicate():
    global websocket
    uri = "ws://90.5.227.209:8765"
    try:
        websocket = await websockets.connect(uri)
        print("Connexion établie.")
        asyncio.create_task(receive_messages())
    except Exception as e:
        print(f"Erreur de connexion : {e}")

# Function to handle sending messages from the input box
def messageAEnvoyer():
    global messageUser
    messageUser = messageUser_box.get().strip()
    if messageUser:
        messageUser_box.delete(0, ctk.END)
        # Use asyncio.run_coroutine_threadsafe to send messages in the asyncio event loop
        asyncio.run_coroutine_threadsafe(send_messages(), asyncio_loop)
    else:
        ctk.CTkMessagebox.show_warning("Input Error", "Vous ne pouvez pas envoyer un message vide !")

# Function to start the asyncio event loop in a separate thread
def start_asyncio_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

# Create and start the asyncio event loop in a new thread
asyncio_loop = asyncio.new_event_loop()
threading.Thread(target=start_asyncio_loop, args=(asyncio_loop,), daemon=True).start()

# Function to start communication with the websocket server
def start_communication():
    asyncio.run_coroutine_threadsafe(communicate(), asyncio_loop)

# customtkinter UI setup
chatBoxLabel = ctk.CTkLabel(root, text="Chatbox:")
chatBoxLabel.pack(pady=5)

chatBox = ctk.CTkTextbox(root, height=200, width=350, state="disabled")
chatBox.pack(pady=5)

messageUser_label = ctk.CTkLabel(root, text="Message à envoyer :")
messageUser_label.pack(pady=5)

messageUser_box = ctk.CTkEntry(root, width=350)
messageUser_box.pack(pady=5)

envoyer_button = ctk.CTkButton(root, text="Envoyer", command=messageAEnvoyer)
envoyer_button.pack(pady=20)

# Start communication after customtkinter UI is initialized
root.after(100, start_communication)

root.mainloop()
