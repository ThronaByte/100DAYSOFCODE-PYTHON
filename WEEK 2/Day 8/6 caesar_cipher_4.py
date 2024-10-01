from cipher_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
def caesar(text, shift,direct):
    cipher_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direct == "encode":
                encrypt_position = (position + shift) % 26
                cipher_text += alphabet[encrypt_position]
            elif direct == "decode":
                decrypt_position = (position - shift) % 26
                cipher_text += alphabet[decrypt_position]
        else:
            cipher_text += char  
    print(f"The {direct} text is: {cipher_text}")
    
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26
    
    caesar(text=text, shift=shift, direct=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result.lower() != 'yes':
        False
        print("Goodbye! 👋🙋‍♂️📍")
        break