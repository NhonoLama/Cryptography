def encrypt_message(message, shift):
    result = ""
    for i in range(len(message)):
        char = message[i]

        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += chr((ord(char) - 97 + shift) % 26 + 97)
    return result


def decrypt_message(message, shift):
    result = ""
    for i in range(len(message)):
        char = message[i]

        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += chr((ord(char) - 97 - shift) % 26 + 97)

    return result


message = input("enter the message to be encrypted:").replace(" ", "")
shift = 5
cipher_text = encrypt_message(message, shift)
print("The encrypted text : " + cipher_text)

normal_text = decrypt_message(cipher_text, shift)
print("The decrypted text : " + normal_text)
