# Decryption Function
from encryption import encrypt_image


def decrypt_image(image, message_length, char_to_int, int_to_char, password):
    # Ask user for password to decrypt
    entered_password = input("Enter passcode for decryption: ")
    if entered_password == password:
        decrypted_message = ""
        n, m, z = 0, 0, 0

        # Retrieve the hidden message from the image
        for _ in range(message_length):
            decrypted_message += int_to_char[image[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3

            # Ensure we do not go out of bounds for the image size
            if n >= image.shape[0]:
                n = 0
                m += 1

        print("Decrypted message:", decrypted_message)
    else:
        print("Incorrect passcode! Access denied.")


# Main Function
def main():
    image_path = "CAR.jpg"  # Path to the image
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    # Encrypt the message into the image
    encrypted_image_path, image, message_length, char_to_int, int_to_char = encrypt_image(image_path, message, password)

    if encrypted_image_path:
        # Decrypt the message after successful encryption
        decrypt_image(image, message_length, char_to_int, int_to_char, password)


if __name__ == "__main__":
    main()