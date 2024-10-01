#def demanderNomUser():
#    nomUtilisateur = None
#    while not nomUtilisateur:
#        nomUtilisateur = simpledialog.askstring("Nom d'utilisateur", "Entrez un nom d'utilisateur :")
#        if not nomUtilisateur:
#            messagebox.showwarning("Input Error", "Vous devez renseigner un nom d'utilisateur")
#    return nomUtilisateur

#nomUtilisateur = demanderNomUser()
# #message = await asyncio.to_thread(f"{nomUtilisateur}: {messageUser}\n")
        #messageUser = messageUser_box.get().strip()
        #message = await asyncio.to_thread(f"{messageUser}\n")

import customtkinter as ctk
from tkinter import messagebox
import asyncio
import websockets

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Chat Bx Python")
root.geometry("400x400")

websocket = None
nomUtilisateur = "Julio"

async def send_message():
    global websocket
    messageUser = messageUser_box.get().strip()
    if messageUser:
        message = f"{nomUtilisateur}: {messageUser}\n"
        await websocket.send(message)
        print(f"Message envoyé : {message}")
        chatBox.configure(state="normal")
        chatBox.insert(ctk.END, message)
        chatBox.configure(state="disabled")
        messageUser_box.delete(0, ctk.END)
    else:
        messagebox.showwarning("Input Error", "Vous ne pouvez pas envoyer un message vide !")

async def receive_messages():
    global websocket
    while True:
        try:
            response = await websocket.recv()
            print(f"Message reçu du serveur : {response}")
            chatBox.configure(state="normal")
            chatBox.insert(ctk.END, f"Serveur: {response}\n")
            chatBox.configure(state="disabled")
        except websockets.ConnectionClosed:
            print("Connexion fermée par le serveur.")
            break

async def communicate():
    global websocket
    uri = "ws://90.5.227.209:8765"
    try:
        async with websockets.connect(uri) as ws:
            websocket = ws
            receive_task = asyncio.create_task(receive_messages())
            await receive_task
    except Exception as e:
        print(f"Erreur de connexion : {e}")

def envoyer_message():
    asyncio.create_task(send_message())

def start_async_loop():
    try:
        asyncio.get_running_loop().run_forever()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_forever()

def async_communicate_wrapper():
    asyncio.create_task(communicate())
    root.after(100, async_communicate_wrapper)

chatBoxLabel = ctk.CTkLabel(root, text="Chatbox:")
chatBoxLabel.pack(pady=5)

chatBox = ctk.CTkTextbox(root, height=200, width=350, state="disabled")
chatBox.pack(pady=5)

messageUser_label = ctk.CTkLabel(root, text="Message à envoyer :")
messageUser_label.pack(pady=5)

messageUser_box = ctk.CTkEntry(root, width=350)
messageUser_box.pack(pady=5)

envoyer_button = ctk.CTkButton(root, text="Envoyer", command=envoyer_message)
envoyer_button.pack(pady=20)

root.after(100, async_communicate_wrapper)
root.after(100, start_async_loop)
root.mainloop()
