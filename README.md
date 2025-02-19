# SECURE DATA HIDING IN IMAGE USING STEGANOGRAPHY

## Introduction
This project implements a **Steganography tool combined with RSA encryption** to securely hide messages within images. The tool ensures that messages remain hidden while being protected with robust encryption.

## Features
- **RSA Encryption:** Ensures message security before embedding.
- **Image-Based Steganography:** Hides encrypted messages within image pixels.
- **User-Friendly GUI:** Allows easy encoding and decoding of messages.
- **Minimal Image Distortion:** Preserves image quality while hiding data.

## Technologies Used
- **Programming Language:** Python 3.11
- **Libraries:**
  - OpenCV (`cv2`) – Image processing
  - Cryptography – RSA encryption
  - Tkinter – GUI for user interaction
  - Base64 – Encoding and decoding messages

## Installation
### Prerequisites
Ensure you have Python 3 installed along with the required dependencies.

```sh
pip install opencv-python cryptography tkinter
```

## Usage
### Encoding a Message
1. Run the script.
2. Select an image.
3. Enter the secret message.
4. Click **Encode** to hide the encrypted message in the image.

### Decoding a Message
1. Select the encoded image.
2. Click **Decode** to extract and decrypt the hidden message.

## Screenshots
Encoding
![Screenshot 2025-02-19 202110](https://github.com/user-attachments/assets/284f44a5-d09c-4620-94b4-9715cb5ebe5e)
Decoding
![Screenshot 2025-02-19 202129](https://github.com/user-attachments/assets/cd11addb-9262-4e6f-92ff-0ef8fdaa44d7)

## Future Enhancements
- Extend support for **video steganography**.
- Implement additional encryption methods like **AES**.
- Develop a **mobile application** version.

## Contributing
Feel free to fork the repository and contribute! Submit a pull request with proposed changes.

## License
This project is licensed under the **MIT License**.



