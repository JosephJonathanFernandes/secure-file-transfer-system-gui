# receiver.py
import socket
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from threading import Thread
import os
from crypto_utils import decrypt_file
import hashlib

class ReceiverApp:
    def __init__(self, master):
        self.master = master
        master.title("Secure File Receiver")

        self.label = tk.Label(master, text="Receiving...")
        self.label.pack(pady=10)

        self.entry_label = tk.Label(master, text="Enter password for decryption")
        self.entry_label.pack()
        self.password_entry = tk.Entry(master, show='*')
        self.password_entry.pack()

        self.output_label = tk.Label(master, text="Save decrypted file as:")
        self.output_label.pack()
        self.save_path = tk.Entry(master, width=50)
        self.save_path.pack(pady=5)

        self.start_button = tk.Button(master, text="Start Receiver", command=self.start_receiver)
        self.start_button.pack(pady=10)

        self.progress = ttk.Progressbar(master, length=300, mode='determinate')
        self.progress.pack(pady=10)

    def start_receiver(self):
        password = self.password_entry.get()
        output_file = self.save_path.get()
        if not password or not output_file:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        def receive():
            with socket.socket() as s:
                s.bind(('0.0.0.0', 5001))
                s.listen(1)
                conn, _ = s.accept()
                with conn, open("received.enc", 'wb') as f:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                        self.progress.step(len(data))
                        self.master.update_idletasks()
                try:
                    decrypt_file("received.enc", output_file, password)
                    os.remove("received.enc")
                    messagebox.showinfo("Success", f"File received and decrypted as {output_file}")
                except Exception as e:
                    messagebox.showerror("Error", f"Decryption failed: {e}")

        Thread(target=receive, daemon=True).start()


if __name__ == '__main__':
    root = tk.Tk()
    app = ReceiverApp(root)
    root.mainloop()
