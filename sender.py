# sender.py
import socket
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from threading import Thread
import os
from crypto_utils import encrypt_file
import hashlib
import shutil

class SenderApp:
    def __init__(self, master):
        self.master = master
        master.title("Secure File Sender")

        self.label = tk.Label(master, text="Choose a file to send")
        self.label.pack(pady=10)

        self.select_button = tk.Button(master, text="Select File", command=self.select_file)
        self.select_button.pack()

        self.send_button = tk.Button(master, text="Send File", command=self.send_file, state=tk.DISABLED)
        self.send_button.pack(pady=5)

        self.entry_label = tk.Label(master, text="Enter password for encryption")
        self.entry_label.pack()
        self.password_entry = tk.Entry(master, show='*')
        self.password_entry.pack()

        self.ip_label = tk.Label(master, text="Receiver IP Address")
        self.ip_label.pack()
        self.ip_entry = tk.Entry(master)
        self.ip_entry.insert(0, "127.0.0.1")
        self.ip_entry.pack()

        self.progress = ttk.Progressbar(master, length=300, mode='determinate')
        self.progress.pack(pady=10)

        self.file_path = ''

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.send_button.config(state=tk.NORMAL)

    def send_file(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showerror("Error", "Please enter a password")
            return

        receiver_ip = self.ip_entry.get()
        if not receiver_ip:
            messagebox.showerror("Error", "Please enter receiver's IP")
            return

        encrypted_file = self.file_path + ".enc"
        encrypt_file(self.file_path, encrypted_file, password)
        filesize = os.path.getsize(encrypted_file)
        self.progress["maximum"] = filesize
        sent_size = 0

        try:
            with socket.socket() as s:
                s.connect((receiver_ip, 5001))
                with open(encrypted_file, 'rb') as f:
                    while chunk := f.read(1024):
                        s.sendall(chunk)
                        sent_size += len(chunk)
                        self.progress["value"] = sent_size
                        self.master.update_idletasks()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send file: {e}")
            return

        os.remove(encrypted_file)
        messagebox.showinfo("Success", "File sent securely!")


if __name__ == '__main__':
    root = tk.Tk()
    app = SenderApp(root)
    root.mainloop()
