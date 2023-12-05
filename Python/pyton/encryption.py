import time

letters = 'abcdefjghijklmnopqrstuvxyz'
letter_num = len(letters)

def encrypt(plaintext, key):
    cyphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                cyphertext += letter
            else:
                new_index = index + key
                if new_index >= letter_num:
                    new_index -= letter_num
                cyphertext += letters[new_index]
    return cyphertext

def decrypt(cyphertext, key):
    plaintext = ''
    for letter in cyphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += letter_num
                plaintext += letters[new_index]
    return plaintext

print("Do you want to encrypt or decrypt a word?")
print()
u_input = input("e/d: ").lower()
if u_input == "e":
    time.sleep(0.5)
    print("Let us encrypt then.")
    print()
    time.sleep(0.5)
    key = int(input("Choose a key (1-26): "))
    print()
    text = input("Enter text to encrypt: ")
    encrypted_text = encrypt(text, key)
    print()
    print("This is the text encrypted:", encrypted_text)
    print()
elif u_input == "d":
    time.sleep(0.5)
    print("Let us decrypt then.")
    print()
    time.sleep(0.5)
    key = int(input("Choose a key (1-26): "))
    print()
    text = input("Enter text to decrypt: ")
    plain_text = decrypt(text, key)
    print()
    print("This is the text decrypted:", plain_text)
    print()