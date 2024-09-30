import tkinter as tk
from tkinter import simpledialog, messagebox
import asyncio
import websockets
import threading

root = tk.Tk()
root.title("Chat Box Python")
root.geometry("400x300")

def demanderNomUser():
    nomUtilisateur = simpledialog.askstring("Nom d'utilisateur", "Entrez un nom d'utilisateur :")
    if nomUtilisateur is None:
        root.quit()
    elif not nomUtilisateur.strip():
        messagebox.showwarning("Input Error", "Vous devez renseigner un nom d'utilisateur")
        return demanderNomUser()
    return nomUtilisateur

nomUtilisateur = demanderNomUser()

async def send_message_to_server(message):
    uri = "ws://192.168.1.34:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response

async def messageAEnvoyer():
    messageUser = messageUser_box.get().strip()
    if messageUser:
        chatBox.config(state=tk.NORMAL)
        chatBox.insert(tk.END, f"{nomUtilisateur}: {messageUser}\n")
        chatBox.config(state=tk.DISABLED)
        try:
            response = await send_message_to_server(messageUser)
            chatBox.config(state=tk.NORMAL)
            chatBox.insert(tk.END, f"Server: {response}\n")
            chatBox.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("WebSocket Error", f"Failed to send message: {e}")
    else:
        messagebox.showwarning("Input Error", "Vous ne pouvez pas envoyer un message vide !")

def start_asyncio_loop():
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_forever()

def run_coroutine(coroutine):
    loop = asyncio.get_event_loop()
    asyncio.run_coroutine_threadsafe(coroutine, loop)

# Start the asyncio event loop in a separate thread
asyncio_thread = threading.Thread(target=start_asyncio_loop, daemon=True)
asyncio_thread.start()

chatBoxLabel = tk.Label(root, text="Chatbox:")
chatBoxLabel.pack(pady=5)

chatBox = tk.Text(root, height=6, width=40)
chatBox.pack(pady=5)
chatBox.config(state=tk.DISABLED)

messageUser_label = tk.Label(root, text="Message à envoyer :")
messageUser_label.pack(pady=5)

messageUser_box = tk.Entry(root, width=40)
messageUser_box.pack(pady=5)

envoyer_button = tk.Button(root, text="Envoyer", command=lambda: run_coroutine(messageAEnvoyer()))
envoyer_button.pack(pady=20)

root.mainloop()
