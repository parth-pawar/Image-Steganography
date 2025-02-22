# Image-Steganography
Here's your **README.md** file in a single markdown block, ready for you to copy and paste in one go:  

## 📌 Project Overview  
This project implements image steganography using Python and OpenCV, allowing users to securely hide and retrieve messages inside an image. The system uses SHA-256 password hashing to ensure secure authentication, preventing unauthorized decryption.  


## 📥 Installation & Setup  
1. Clone the repository:
 
   git clone https://github.com/your-username/Image-Stegano.git
   cd Image-Stegano
   
3. Install required dependencies: 
  
   pip install opencv-python numpy

4. Ensure you have an image (PNG/JPG) in the same folder as the script.
   

## 🔑 Usage  

###  Encryption (Hiding Message)
Run the encryption script:  

python encrypt.py

- Enter the secret message.  
- Enter a passcode (used for decryption).  
- The encrypted image (`encryptedImage.png`) is saved in the directory.  

### Decryption (Retrieving Message)
Run the decryption script:  

python decrypt.py

- Enter the correct passcode to reveal the hidden message.  
- If the passcode is incorrect, decryption will fail.  
 
