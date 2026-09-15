def caesar_cipher(text: str, shift: int) -> str:
    result = []

    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
                new_char = chr((ord(char) - base + shift) % 26 + base)
                result.append(new_char)
            elif char.islower():
                base = ord('a')
                new_char = chr((ord(char) - base + shift) % 26 + base)
                result.append(new_char)
        else:

            result.append(char)

    return "".join(result)
text_input = input("Enter your message: ")
shift_input = int(input("Enter shift number: "))
encrypted_message = caesar_cipher(text_input, shift_input)
print("Encrypted Message:", encrypted_message)
