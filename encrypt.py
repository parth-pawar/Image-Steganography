import cv2
import hashlib

# Load the image
img = cv2.imread("mypic.png")  # Ensure this file exists in the same directory

if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Use SHA-256 for a consistent password hash
password_hash = hashlib.sha256(password.encode()).hexdigest()

# Save the password hash to a file for verification in decryption
with open("password.txt", "w") as f:
    f.write(password_hash)

# Character mapping
d = {chr(i): i for i in range(255)}

rows, cols, _ = img.shape

# Store message length in the first 3 pixels (each channel can store 255 values)
msg_len = len(msg)
img[0, 0, 0] = msg_len // 255  # Store higher byte
img[0, 0, 1] = msg_len % 255   # Store lower byte

index = 0

for i in range(rows):
    for j in range(cols):
        for k in range(3):  # Iterate over RGB channels
            if i == 0 and j == 0 and k < 2:
                continue  # Skip first two channels where message length is stored

            if index < msg_len:
                img[i, j, k] = d[msg[index]]
                index += 1
            else:
                break
        if index >= msg_len:
            break
    if index >= msg_len:
        break

# Save encrypted image
cv2.imwrite("encryptedImage.png", img)
print("Encryption complete! Image saved as 'encryptedImage.png'.")
