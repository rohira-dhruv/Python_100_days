import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cont = "yes"

def caesar(text, shift, direction):
    cipher_text = ""
    for char in text:
        if char in alphabet:
            pos = alphabet.index(char)
            
            if direction == "encode":
                if pos + shift > 25:
                    pos = pos - 26
                cipher_text += alphabet[pos+shift%26]
                
            elif direction == "decode":
                if pos - shift < 0:
                    pos = pos + 26
                cipher_text += alphabet[pos-shift%26]
                
        else:
            cipher_text += char
    print(f"The result text is {cipher_text}")

while cont == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    cont = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

print("Goodbye!")