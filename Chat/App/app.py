import tkinter as tk
from tkinter import simpledialog,messagebox

root = tk.Tk()
root.title("Chat Box Python")
root.geometry("400x300")


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
        chatBox.insert(tk.END,  f"{nomUtilisateur}: {messageUser}\n")
    else:
        messagebox.showwarning("Input Error", "Vous ne pouvez pas envoyer un message vide !")
chatBoxLabel = tk.Label(root, text="Chatbox:")
chatBoxLabel.pack(pady=5)

chatBox = tk.Text(root, height=6, width=40)
chatBox.pack(pady=5)

messageUser_label = tk.Label(root, text="Message a envoyer :")
messageUser_label.pack(pady=5)

messageUser_box = tk.Entry(root, width=40)
messageUser_box.pack(pady=5)

envoyer_button = tk.Button(root, text="Envoyer", command=messageAEnvoyer)
envoyer_button.pack(pady=20)

root.mainloop()
