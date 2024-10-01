import customtkinter as ctk
from tkinter import messagebox
from tkinter import simpledialog
import asyncio
import websockets

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Chat Bx Python")
root.geometry("400x400")


import asyncio
import websockets

# Fonction pour envoyer des messages au serveur
async def send_messages(websocket):
    while True:
        # Utiliser asyncio pour capturer l'entrée utilisateur sans bloquer
        #message = await asyncio.to_thread(f"{nomUtilisateur}: {messageUser}\n")
        message = await asyncio.to_thread(f"{messageUser}\n")
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

#def demanderNomUser():
#    nomUtilisateur = None
#    while not nomUtilisateur:
#        nomUtilisateur = simpledialog.askstring("Nom d'utilisateur", "Entrez un nom d'utilisateur :")
#        if not nomUtilisateur:
#            messagebox.showwarning("Input Error", "Vous devez renseigner un nom d'utilisateur")
#    return nomUtilisateur

#nomUtilisateur = demanderNomUser()
#
#def messageAEnvoyer():
#    messageUser = messageUser_box.get().strip()
#    if messageUser:
#        chatBox.configure(state="normal") 
#        chatBox.insert(ctk.END, f"{nomUtilisateur}: {messageUser}\n")
#        chat=(ctk.END, f"{nomUtilisateur}: {messageUser}\n")
#        asyncio.run(send_message(chat))
#        chatBox.configure(state="disabled")  
#        messageUser_box.delete(0, ctk.END)
#    else:
#            messagebox.showwarning("Input Error", "Vous ne pouvez pas envoyer un message vide !")
#
chatBoxLabel = ctk.CTkLabel(root, text="Chatbox:")
chatBoxLabel.pack(pady=5)

chatBox = ctk.CTkTextbox(root, height=200, width=350, state="disabled") 
chatBox.pack(pady=5)

messageUser_label = ctk.CTkLabel(root, text="Message à envoyer :")
messageUser_label.pack(pady=5)

messageUser_box = ctk.CTkEntry(root, width=350)
messageUser_box.pack(pady=5)

envoyer_button = ctk.CTkButton(root, text="Envoyer", command=send_messages(websockets))
envoyer_button.pack(pady=20)



root.mainloop()
