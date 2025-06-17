def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


message = input("Enter the message: ")
shift = int(input("Enter the shift value (integer): "))


encrypted_message = caesar_cipher_encrypt(message, shift)
decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)

print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")
