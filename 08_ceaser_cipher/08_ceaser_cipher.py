from ASCII_and_alphabet_list import logo, alphabet

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
message = input("Type your message: ").lower()
shift_number = int(input("Type the shift number: "))


def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        if letter.lower() in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            if shifted_position >= 26:
                cipher_text += alphabet[shifted_position - 26]
            else:
                cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter

    print(f"The result is {cipher_text}")


def decrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        if letter.lower() in alphabet:
            shifted_position = alphabet.index(letter) - shift_amount
            if shifted_position < 0:
                cipher_text += alphabet[shifted_position]
            else:
                cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter

    print(f"The result is {cipher_text}")


flag = True

while flag:
    if direction == "encode":
        encrypt(original_text=message, shift_amount=shift_number)
    elif direction == "decode":
        decrypt(original_text=message, shift_amount=shift_number)
    else:
        print("undefined")

    continue_game = input("Continue? Y(es) or N(o): ")

    if continue_game == "Y":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
        message = input("Type your message: ").lower()
        shift_number = int(input("Type the shift number: "))
    else:
        flag = False
        print("Goodbye")

