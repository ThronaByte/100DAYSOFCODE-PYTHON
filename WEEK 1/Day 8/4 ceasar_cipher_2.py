alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(encrypt_text, shift_number):
    
  cipher_text = ""
  for letter in encrypt_text:
    position = alphabet.index(letter)
    encrypt_position = position + shift_number
    cipher_text += alphabet[encrypt_position]
  print(f"The encoded text is: {cipher_text}")

def decrypt(decrypt_text, shift_number):
    
    dipher_text =""
    for letter in decrypt_text:
        position = alphabet.index(letter)
        decrypt_position = position - shift_number
        dipher_text += alphabet[decrypt_position]
    print(f"The decoded text is: {dipher_text}")


if direction == 'encode':
    encrypt(encrypt_text=text,shift_number=shift)
elif direction == 'decode':
    decrypt(decrypt_text=text, shift_number=shift)
else:
    print('invalid input')