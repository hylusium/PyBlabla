import customtkinter as ctk
import asyncio
import websockets
import threading

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Chat Python")
root.geometry("400x400")

nomUtilisateur = ""
websocket = None
messageUser = None

async def send_messages():
    global websocket, messageUser
    if websocket and messageUser:
        message = f"{nomUtilisateur}: {messageUser}\n"
        chatBox.configure(state="normal")
        chatBox.insert(ctk.END, f"{message}\n")
        chatBox.configure(state="disabled")
        await websocket.send(message)
        print(f"Message envoyé : {message}")

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

async def communicate():
    global websocket
    uri = "ws://90.5.227.209:8765"
    try:
        websocket = await websockets.connect(uri)
        print("Connexion établie.")
        asyncio.create_task(receive_messages())
    except Exception as e:
        print(f"Erreur de connexion : {e}")

def messageAEnvoyer():
    global messageUser
    messageUser = messageUser_box.get().strip()
    if messageUser:
        messageUser_box.delete(0, ctk.END)
        asyncio.run_coroutine_threadsafe(send_messages(), asyncio_loop)
    else:
        ctk.CTkMessagebox.show_warning("Input Error", "Vous ne pouvez pas envoyer un message vide !")

def start_asyncio_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

asyncio_loop = asyncio.new_event_loop()
threading.Thread(target=start_asyncio_loop, args=(asyncio_loop,), daemon=True).start()

def start_communication():
    asyncio.run_coroutine_threadsafe(communicate(), asyncio_loop)

def ask_for_nickname():
    def submit_nickname():
        global nomUtilisateur
        entered_nickname = nickname_entry.get().strip()
        if entered_nickname:
            nomUtilisateur = entered_nickname
            nickname_window.destroy()
        else:
            ctk.CTkMessagebox.show_warning("Input Error", "Vous devez entrer un pseudo valide!")

    nickname_window = ctk.CTkToplevel(root)
    nickname_window.title("Enter Nickname")
    nickname_window.geometry("300x150")

    ctk.CTkLabel(nickname_window, text="Entrez votre pseudo :").pack(pady=10)
    nickname_entry = ctk.CTkEntry(nickname_window)
    nickname_entry.pack(pady=5)

    submit_button = ctk.CTkButton(nickname_window, text="Submit", command=submit_nickname)
    submit_button.pack(pady=10)

    nickname_window.grab_set()
    nickname_window.transient(root)

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

ask_for_nickname()
root.after(100, start_communication)

root.mainloop()
