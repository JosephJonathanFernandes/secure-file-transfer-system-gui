## Secure File Transfer System (GUI Version)

A professional, Python-based secure file transfer application featuring a graphical user interface (GUI). This tool allows encrypted file transfers over a local network using AES encryption, suitable for personal and organizational use.

## ✨ Features

AES-256 Encryption (CBC Mode)

Password-protected Transfers

Tkinter-based GUI for Sender and Receiver

Progress Bar and File Size Display

Localhost and LAN IP Support

Cross-platform (Tested on Windows)

## 📦 Requirements

Python 3.11+

pycryptodome package

Installation

Clone the repository:

git clone https://github.com/JosephJonathanFernandes/secure-file-transfer-system-gui.git

cd secure-file-transfer-system-gui

Install dependencies:

pip install -r requirements.txt

## 🚀 Usage Guide

Step 1: Launch the Receiver

Run receiver.py.

Set the output file save path.

Enter a password.

Click Start Receiver.

Step 2: Launch the Sender

Run sender.py.

Select the file to send.

Enter the receiver's IP address (use 127.0.0.1 for localhost).

Enter the same password used on the receiver.

Click Send File.

Notes:

Make sure both devices are on the same network.

The password must match on both ends for decryption to succeed.

## 🔐 How It Works

Encryption: AES (CBC mode) with a password-derived key.

Transfer: TCP socket streams the encrypted file.

Decryption: Receiver uses the same password to decrypt and save the file.

GUI: Built using Tkinter for a clean, user-friendly experience.

## 🔒 Security Considerations

Password-derived key uses SHA-256 hashing.

Only the correct password will successfully decrypt transferred files.

For production deployment, use HTTPS-secured transport layers.

## 💪 Development & Contribution

### Project Structure

secure-file-transfer-system-gui/

├── crypto_utils.py

├── sender.py

├── receiver.py

├── requirements.txt

├── .gitignore

├── README.md

## Contributions

Pull requests and suggestions are welcome. Please open an issue first to discuss changes.

## 📅 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 👤 Author

Developed by JJF and with help of GEN AI. Feel free to reach out for collaboration or questions.

## 🔍 Links

https://github.com/JosephJonathanFernandes/secure-file-transfer-system-gui.git

For any critical use cases, professional code audits and penetration testing are recommended.
