alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift,direct):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direct == "encode":
            encrypt_position = position + shift
            cipher_text += alphabet[encrypt_position]
        elif direct == "decode":
            decrypt_position = position - shift
            cipher_text += alphabet[decrypt_position]
    print(f"The {direct} text is: {cipher_text}")
caesar(text=text, shift=shift, direct=direction)