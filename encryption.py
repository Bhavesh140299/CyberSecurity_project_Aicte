import cv2
import os

# Encryption Function
def encrypt_image(image_path, message, password):
    try:
        # Load the image
        img = cv2.imread("CAR.jpg")
        if img is None:
            raise FileNotFoundError(f"Image file '{image_path}' not found!")

        # Encoding and decoding tables for characters
        char_to_int = {chr(i): i for i in range(255)}
        int_to_char = {i: chr(i) for i in range(255)}

        # Variables for image pixel manipulation
        n, m, z = 0, 0, 0  # n, m are row and column indices, z is the RGB channel index
        message_length = len(message)

        # Encrypt the message into the image by modifying pixel values
        for char in message:
            img[n, m, z] = char_to_int[char]  # Embed character into the pixel
            n += 1
            m += 1
            z = (z + 1) % 3  # Cycle through R, G, B channels

            # Ensure we do not go out of bounds for the image size
            if n >= img.shape[0]:
                n = 0
                m += 1

        # Save the encrypted image
        encrypted_image_path = "encrypted_image.jpg"
        cv2.imwrite(encrypted_image_path, img)
        print(f"Encrypted image saved as '{encrypted_image_path}'.")

        # Return necessary values for decryption
        return encrypted_image_path, img, message_length, char_to_int, int_to_char

    except Exception as e:
        print(f"Error in encryption: {e}")
        return None, None, None, None, None