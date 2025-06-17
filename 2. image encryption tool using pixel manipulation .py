from PIL import Image

def encrypt_decrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]  # Handle RGBA if present
            # Apply XOR to each channel
            r ^= key
            g ^= key
            b ^= key
            pixels[x, y] = (r, g, b)

    img.save(output_path)

# Final 
encrypt_decrypt_image("input.jpg", "encrypted.png", 123) 
encrypt_decrypt_image("encrypted.png", "decrypted.jpg", 123)  
