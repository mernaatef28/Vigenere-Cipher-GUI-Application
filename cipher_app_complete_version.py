
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image
import numpy as np

def repeat_key(key, length):
    return (key * (length // len(key) + 1))[:length]

def decrypt_image():
    cipher_image_path = filedialog.askopenfilename(filetypes=[("Image Files", ".png;.jpg;*.jpeg")])
    
    if cipher_image_path:
        key = key_entry.get()

        with Image.open(cipher_image_path) as img:
            cipher_image_array = np.array(img)

            flat_cipher_image_array = cipher_image_array.flatten()

            temp_key = repeat_key(key, len(flat_cipher_image_array))

            temp_key_array = np.array([ord(c) for c in temp_key])

            original_image_array = flat_cipher_image_array - temp_key_array

            original_image_array = original_image_array.reshape(cipher_image_array.shape)

            original_image = Image.fromarray(np.uint8(original_image_array))

            original_image.save('original_image.png')
            messagebox.showinfo("Decryption Complete", "Image decrypted and saved as 'original_image.png'")

def encrypt_image():
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", ".png;.jpg;*.jpeg")])
    
    if image_path:
        key = key_entry.get()

        with Image.open(image_path) as img:
            image_array = np.array(img)

            flat_image_array = image_array.flatten()

            temp_key = repeat_key(key, len(flat_image_array))

            temp_key_array = np.array([ord(c) for c in temp_key])

            cipher_image_array = [val + temp_key_array[i] for i, val in enumerate(flat_image_array)]

            cipher_image_array = np.array(cipher_image_array).reshape(image_array.shape)

            cipher_image = Image.fromarray(np.uint8(cipher_image_array))

            cipher_image.save('cipher_image.png')
            messagebox.showinfo("Encryption Complete", "Image encrypted and saved as 'cipher_image.png'")

def vigenere_encrypt(plain_text, key="CIPHER"):
    size = len(plain_text)
    encrypted_message = [''] * size

    for i in range(size):
        j = i % len(key)
        p = plain_text[i]
        k = key[j]

        p_index = ord(p) - ord('A')
        k_index = ord(k) - ord('A')

        enc_index = (p_index + k_index) % 26

        encrypted_message[i] = chr(enc_index + ord('A'))

    return ''.join(encrypted_message)

def vigenere_decrypt(plain_text, key="CIPHER"):
    size = len(plain_text)
    decrypted_message = [''] * size

    for i in range(size):
        j = i % len(key)
        p = plain_text[i]
        k = key[j]

        p_index = ord(p) - ord('A')
        k_index = ord(k) - ord('A')

        dec_index = (p_index - k_index) % 26

        decrypted_message[i] = chr(dec_index + ord('A'))

    return ''.join(decrypted_message)

def encrypt_text():
    plain_text = plaintext_entry.get().upper()
    key = key_entry.get().upper()
    ciphertext = vigenere_encrypt(plain_text, key)
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(0, ciphertext)

def decrypt_text():
    cipher_text = ciphertext_entry.get().upper()
    key = key_entry.get().upper()
    plaintext = vigenere_decrypt(cipher_text, key)
    plaintext_entry.delete(0, tk.END)
    plaintext_entry.insert(0, plaintext)

# Create a themed Tkinter window
window = tk.Tk()
window.title("Vigenere Cipher Algorithm")
window.geometry("500x420")
window.configure(bg="#f0f0f0")  # Set background color

# Define styles
style = ttk.Style(window)
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 10), background="#4CAF50", foreground="white", relief="flat", padx=10, pady=5, borderwidth=0)
style.map("TButton", background=[("active", "#45a049")])  # Hover effect

# Frame for widgets
frame = ttk.Frame(window, padding=10)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title label
title_label = tk.Label(frame, text="Vigenere Cipher Algorithm", font=("Arial", 14, "bold"), background="#f0f0f0")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Label and Entry for key
label = ttk.Label(frame, text="Enter Key:", background="#f0f0f0")
label.grid(row=1, column=0, sticky="e", padx=(0, 5), pady=(5, 0))
key_entry = ttk.Entry(frame)
key_entry.grid(row=1, column=1, sticky="ew", padx=(0, 5), pady=(5, 0))

# Text fields for plaintext and ciphertext
plaintext_label = ttk.Label(frame, text="Plaintext:", background="#f0f0f0")
plaintext_label.grid(row=2, column=0, sticky="e", padx=(0, 5), pady=(5, 0))
plaintext_entry = ttk.Entry(frame)
plaintext_entry.grid(row=2, column=1, sticky="ew", padx=(0, 5), pady=(5, 0))

ciphertext_label = ttk.Label(frame, text="Ciphertext:", background="#f0f0f0")
ciphertext_label.grid(row=3, column=0, sticky="e", padx=(0, 5), pady=(5, 0))
ciphertext_entry = ttk.Entry(frame)
ciphertext_entry.grid(row=3, column=1, sticky="ew", padx=(0, 5), pady=(5, 0))

# Buttons for text encryption and decryption
encrypt_text_button = ttk.Button(frame, text="Encrypt Text", command=encrypt_text)
encrypt_text_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="we")
decrypt_text_button = ttk.Button(frame, text="Decrypt Text", command=decrypt_text)
decrypt_text_button.grid(row=5, column=0, columnspan=2, pady=5, sticky="we")

# Buttons for image encryption and decryption
encrypt_button = ttk.Button(frame, text="Encrypt Image", command=encrypt_image)
encrypt_button.grid(row=6, column=0, columnspan=2, pady=10, sticky="we")
decrypt_button = ttk.Button(frame, text="Decrypt Image", command=decrypt_image)
decrypt_button.grid(row=7, column=0, columnspan=2, pady=5, sticky="we")

# Center the window on the screen
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x_offset = (window.winfo_screenwidth() - width) // 2
y_offset = (window.winfo_screenheight() - height) // 2
window.geometry(f"+{x_offset}+{y_offset}")

# Run the Tkinter event loop
window.mainloop()
