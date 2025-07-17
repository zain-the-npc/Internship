# gui.py

import customtkinter as ctk
from encryptor import encrypt_message, decrypt_message

def run_gui():
    ctk.set_appearance_mode("System")  # or "Dark", "Light"
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x600")
    app.title("VaultCode – Offline Message Locker")

    # Heading
    heading = ctk.CTkLabel(app, text="VaultCode", font=ctk.CTkFont(size=22, weight="bold"))
    heading.pack(pady=15)

    # Message Entry
    msg_label = ctk.CTkLabel(app, text="Message:")
    msg_label.pack()
    msg_entry = ctk.CTkTextbox(app, height=80)
    msg_entry.pack(pady=5)

    # Password Entry
    pwd_label = ctk.CTkLabel(app, text="Password:")
    pwd_label.pack()
    pwd_entry = ctk.CTkEntry(app, show="•")
    pwd_entry.pack(pady=5)

    # Result Box
    result_label = ctk.CTkLabel(app, text="Output:")
    result_label.pack(pady=(15, 0))
    result_box = ctk.CTkEntry(app, width=400)
    result_box.pack()

    # Copy to Clipboard Function
    def copy_to_clipboard():
        text = result_box.get()
        if text:
            app.clipboard_clear()
            app.clipboard_append(text)
            result_box.configure(placeholder_text="Copied to clipboard ✅")

    # Copy Button
    copy_btn = ctk.CTkButton(app, text="Copy to Clipboard", command=copy_to_clipboard)
    copy_btn.pack(pady=5)

    # Action Handlers
    def encrypt_action():
        msg = msg_entry.get("1.0", "end").strip()
        pwd = pwd_entry.get().strip()
        if msg and pwd:
            result = encrypt_message(msg, pwd)
            result_box.delete(0, "end")
            result_box.insert(0, result)
        else:
            result_box.delete(0, "end")
            result_box.insert(0, "[Enter message and password]")

    def decrypt_action():
        code = msg_entry.get("1.0", "end").strip()
        pwd = pwd_entry.get().strip()
        if code and pwd:
            result = decrypt_message(code, pwd)
            result_box.delete(0, "end")
            result_box.insert(0, result)
        else:
            result_box.delete(0, "end")
            result_box.insert(0, "[Enter encrypted code and password]")

    # Buttons
    btn_frame = ctk.CTkFrame(app)
    btn_frame.pack(pady=15)

    encrypt_btn = ctk.CTkButton(btn_frame, text="Encrypt", command=encrypt_action)
    encrypt_btn.grid(row=0, column=0, padx=10)

    decrypt_btn = ctk.CTkButton(btn_frame, text="Decrypt", command=decrypt_action)
    decrypt_btn.grid(row=0, column=1, padx=10)

    app.mainloop()
