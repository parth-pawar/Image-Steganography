import cv2
import hashlib

# Load the encrypted image
img = cv2.imread("encryptedImage.png")

if img is None:
    print("Error: Encrypted image not found!")
    exit()

# Read the stored password hash
try:
    with open("password.txt", "r") as f:
        stored_hash = f.read().strip()
except FileNotFoundError:
    print("Error: Password file not found!")
    exit()

# Ask for passcode
entered_password = input("Enter passcode for decryption: ")
entered_hash = hashlib.sha256(entered_password.encode()).hexdigest()

if entered_hash == stored_hash:
    # Retrieve message length from the first pixel
    msg_len = (img[0, 0, 0] * 255) + img[0, 0, 1]

    message = ""
    index = 0

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):  # Iterate over RGB channels
                if i == 0 and j == 0 and k < 2:
                    continue  # Skip the length data

                if index < msg_len:
                    message += chr(img[i, j, k])
                    index += 1
                else:
                    break
            if index >= msg_len:
                break
        if index >= msg_len:
            break

    print("Decryption successful! Message:", message)
else:
    print("Authentication failed! Incorrect passcode.")
