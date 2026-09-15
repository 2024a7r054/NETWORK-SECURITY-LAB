def vigenere_cipher(text, key, decrypt=False):
    result = []
    key = key.lower()
    k_idx = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[k_idx % len(key)]) - ord('a')
            if decrypt:
                shift = -shift
            
            result.append(chr((ord(char) - base + shift) % 26 + base))
            k_idx += 1
        else:
            result.append(char)

    return "".join(result)

text = input("Message: ")
key = input("Key: ")
mode = input("Mode (E/D): ")

print("Result:", vigenere_cipher(text, key, mode.upper() == "D"))
