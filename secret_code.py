#!/usr/bin/env python3
"""
SecretCodeMaker - Encryption and Decryption Script
Encrypts text using character-to-number mapping and position-based transformation.
"""

import sys


def create_character_mapping():
    """
    Create a mapping of characters to numbers.
    A=1, B=2, ..., Z=26, a=27, b=28, ..., z=52, followed by punctuation and special characters.
    """
    char_to_num = {}
    num_to_char = {}

    current_num = 1

    # Uppercase letters A-Z (1-26)
    for i in range(26):
        char = chr(ord('A') + i)
        char_to_num[char] = current_num
        num_to_char[current_num] = char
        current_num += 1

    # Lowercase letters a-z (27-52)
    for i in range(26):
        char = chr(ord('a') + i)
        char_to_num[char] = current_num
        num_to_char[current_num] = char
        current_num += 1

    # Common punctuation and special characters (53+)
    punctuation = ' .,!?;:\'"()-[]{}@#$%^&*_+=/<>\\|`~\n\t0123456789'
    for char in punctuation:
        if char not in char_to_num:
            char_to_num[char] = current_num
            num_to_char[current_num] = char
            current_num += 1

    return char_to_num, num_to_char


def encrypt(text, char_to_num):
    """
    Encrypt text using character mapping and position-based transformation.
    Transformation pattern: [1, 9, 1, 6, 2, 5, 5, 2, 6, 1, 9, 1] (repeating)
    """
    # Transformation pattern
    pattern = [1, 9, 1, 6, 2, 5, 5, 2, 6, 1, 9, 1]

    encrypted_numbers = []

    for position, char in enumerate(text):
        if char not in char_to_num:
            print(f"Warning: Character '{char}' not in mapping, skipping.", file=sys.stderr)
            continue

        # Get base number for character
        base_num = char_to_num[char]

        # Apply transformation based on position
        transformation = pattern[position % len(pattern)]
        encrypted_num = base_num + transformation

        encrypted_numbers.append(str(encrypted_num))

    return ','.join(encrypted_numbers)


def decrypt(encrypted_text, num_to_char):
    """
    Decrypt encrypted text back to original text.
    Reverses the position-based transformation and maps numbers back to characters.
    """
    # Transformation pattern (same as encryption)
    pattern = [1, 9, 1, 6, 2, 5, 5, 2, 6, 1, 9, 1]

    # Parse comma-separated numbers
    try:
        encrypted_numbers = [int(num.strip()) for num in encrypted_text.split(',')]
    except ValueError:
        return "Error: Invalid encrypted text format. Expected comma-separated numbers."

    decrypted_chars = []

    for position, encrypted_num in enumerate(encrypted_numbers):
        # Reverse transformation based on position
        transformation = pattern[position % len(pattern)]
        base_num = encrypted_num - transformation

        # Map number back to character
        if base_num not in num_to_char:
            print(f"Warning: Number {base_num} not in mapping, skipping.", file=sys.stderr)
            continue

        decrypted_chars.append(num_to_char[base_num])

    return ''.join(decrypted_chars)


def print_character_mapping(char_to_num):
    """Print the character mapping for reference."""
    print("\n=== Character Mapping ===")
    print("\nUppercase Letters:")
    for i in range(26):
        char = chr(ord('A') + i)
        print(f"{char} = {char_to_num[char]}", end="  ")
        if (i + 1) % 6 == 0:
            print()

    print("\n\nLowercase Letters:")
    for i in range(26):
        char = chr(ord('a') + i)
        print(f"{char} = {char_to_num[char]}", end="  ")
        if (i + 1) % 6 == 0:
            print()

    print("\n\nPunctuation & Special Characters:")
    count = 0
    for char, num in sorted(char_to_num.items(), key=lambda x: x[1]):
        if not char.isalpha():
            if char == ' ':
                display = '[SPACE]'
            elif char == '\n':
                display = '[NEWLINE]'
            elif char == '\t':
                display = '[TAB]'
            else:
                display = char
            print(f"{display} = {num}", end="  ")
            count += 1
            if count % 6 == 0:
                print()
    print("\n")


def main():
    """Main CLI interface."""
    # Create character mappings
    char_to_num, num_to_char = create_character_mapping()

    print("=" * 60)
    print("    SecretCodeMaker - Encryption/Decryption Tool")
    print("=" * 60)

    while True:
        print("\nOptions:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. View character mapping")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '1':
            print("\n--- ENCRYPTION ---")
            text = input("Enter text to encrypt: ")
            encrypted = encrypt(text, char_to_num)
            print(f"\nEncrypted: {encrypted}")

        elif choice == '2':
            print("\n--- DECRYPTION ---")
            encrypted_text = input("Enter encrypted text (comma-separated numbers): ")
            decrypted = decrypt(encrypted_text, num_to_char)
            print(f"\nDecrypted: {decrypted}")

        elif choice == '3':
            print_character_mapping(char_to_num)

        elif choice == '4':
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
