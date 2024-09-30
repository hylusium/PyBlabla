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

def demanderNomUser():
    nomUtilisateur = None
    while not nomUtilisateur:
        nomUtilisateur = simpledialog.askstring("Nom d'utilisateur", "Entrez un nom d'utilisateur :")
        if not nomUtilisateur:
            messagebox.showwarning("Input Error", "Vous devez renseigner un nom d'utilisateur")
    return nomUtilisateur

nomUtilisateur = demanderNomUser()

def messageAEnvoyer():
    messageUser = messageUser_box.get().strip()
    if messageUser:
        chatBox.configure(state="normal")  # Enable chatbox to insert text
        chatBox.insert(ctk.END, f"{nomUtilisateur}: {messageUser}\n")
        chatBox.configure(state="disabled")  # Disable chatbox after inserting text
        messageUser_box.delete(0, ctk.END)
    else:
        messagebox.showwarning("Input Error", "Vous ne pouvez pas envoyer un message vide !")

chatBoxLabel = ctk.CTkLabel(root, text="Chatbox:")
chatBoxLabel.pack(pady=5)

chatBox = ctk.CTkTextbox(root, height=200, width=350, state="disabled")  # Chatbox is initially read-only
chatBox.pack(pady=5)

messageUser_label = ctk.CTkLabel(root, text="Message à envoyer :")
messageUser_label.pack(pady=5)

messageUser_box = ctk.CTkEntry(root, width=350)
messageUser_box.pack(pady=5)

envoyer_button = ctk.CTkButton(root, text="Envoyer", command=messageAEnvoyer)
envoyer_button.pack(pady=20)

root.mainloop()
