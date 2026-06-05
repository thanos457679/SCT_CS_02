from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    encrypted_path = "encrypted_image.png"
    img.save(encrypted_path)
    print(f"Encrypted image saved as {encrypted_path}")


def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    decrypted_path = "decrypted_image.png"
    img.save(decrypted_path)
    print(f"Decrypted image saved as {decrypted_path}")


print("=== Image Encryption Tool ===")

image_path = input("Enter image path: ")
key = int(input("Enter encryption key: "))

encrypt_image(image_path, key)

decrypt_choice = input("Do you want to decrypt the encrypted image? (yes/no): ")

if decrypt_choice.lower() == "yes":
    decrypt_image("encrypted_image.png", key)