
def caesar_cipher(text, shift):
    """
    Encrypts text using a Caesar cipher.
    Preserves spaces, punctuation, and letter casing.
    """
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                index = alphabet.index(char)
                new_index = (index + shift) % 26
                result += alphabet[new_index]
            else:
                alphabet = "abcdefghijklmnopqrstuvwxyz"
                index = alphabet.index(char)
                new_index = (index + shift) % 26
                result += alphabet[new_index]
        else:
            result += char

    return result


def caesar_decipher(ciphertext, shift):
    """
    Decrypts a Caesar cipher message.
    """
    return caesar_cipher(ciphertext, -shift)


def letter_frequency(text):
    """
    Counts letter frequencies, ignoring case and non-letters.
    Returns a dictionary.
    """
    frequency = {}

    for letter in "abcdefghijklmnopqrstuvwxyz":
        frequency[letter] = 0

    for char in text.lower():
        if char.isalpha():
            frequency[char] += 1

    return frequency


def main():
    print("=== Caesar Cipher Program ===")

    while True:
        print("\nMenu")
        print("1. Encrypt Message")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            message = input("Enter a message: ")

            try:
                shift = int(input("Enter shift value: "))
            except ValueError:
                print("Shift must be an integer.")
                continue

            encrypted = caesar_cipher(message, shift)
            frequencies = letter_frequency(message)
            decrypted = caesar_decipher(encrypted, shift)

            print("\nEncrypted Text:")
            print(encrypted)

            print("\nLetter Frequencies:")
            for letter, count in frequencies.items():
                if count > 0:
                    print(f"{letter}: {count}")

            print("\nDecrypted Text:")
            print(decrypted)

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()