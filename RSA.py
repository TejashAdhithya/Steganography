import cv2
import numpy as np
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64


private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

def encode_message(image_path, output_path, message):
    
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Could not open image. Check the file path.")
        return

    
    encrypted_message = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    
    encoded_message = base64.b64encode(encrypted_message).decode() + "###END###"

    
    binary_message = ''.join(format(ord(char), '08b') for char in encoded_message)
    msg_len = len(binary_message)
    idx = 0

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                if idx < msg_len:
                    img[i, j, k] = (img[i, j, k] & 254) | int(binary_message[idx])
                    idx += 1
                else:
                    cv2.imwrite(output_path, img)
                    messagebox.showinfo("Success", f"Message successfully encoded into {output_path}")
                    return

def decode_message(image_path):
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Could not open image. Check the file path.")
        return
    
    binary_message = ""
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                binary_message += str(img[i, j, k] & 1)
    
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    extracted_message = ''.join(chr(int(char, 2)) for char in chars)
    extracted_message = extracted_message.split("###END###")[0]
    
    encrypted_message = base64.b64decode(extracted_message)
    
    try:
        decrypted_message = private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()
        messagebox.showinfo("Decrypted Message", f"Decrypted message: {decrypted_message}")
    except Exception as e:
        messagebox.showerror("Error", "Failed to decrypt message. Wrong key or corrupted data.")

def browse_image():
    filename = filedialog.askopenfilename()
    image_path_entry.delete(0, 'end')
    image_path_entry.insert(0, filename)

def encode():
    image_path = image_path_entry.get()
    output_path = "encryptedImage.png"
    message = message_entry.get()
    encode_message(image_path, output_path, message)

def decode():
    image_path = "encryptedImage.png"
    decode_message(image_path)

root = Tk()
root.title("RSA Steganography Tool")

Label(root, text="Image Path:").grid(row=0, column=0, padx=10, pady=10)
image_path_entry = Entry(root, width=50)
image_path_entry.grid(row=0, column=1, padx=10, pady=10)
Button(root, text="Browse", command=browse_image).grid(row=0, column=2, padx=10, pady=10)

Label(root, text="Message:").grid(row=1, column=0, padx=10, pady=10)
message_entry = Entry(root, width=50)
message_entry.grid(row=1, column=1, padx=10, pady=10)

Button(root, text="Encode", command=encode).grid(row=2, column=0, padx=10, pady=10)
Button(root, text="Decode", command=decode).grid(row=2, column=1, padx=10, pady=10)

root.mainloop()