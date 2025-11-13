#!/usr/bin/env python3
"""
Test script for secret_code.py
"""

from secret_code import create_character_mapping, encrypt, decrypt


def test_encryption_decryption():
    """Test that encryption and decryption work correctly."""
    char_to_num, num_to_char = create_character_mapping()

    # Test cases
    test_texts = [
        "Hello World!",
        "ABC",
        "Test 123",
        "The quick brown fox jumps over the lazy dog."
    ]

    print("=" * 60)
    print("Testing Encryption/Decryption")
    print("=" * 60)

    for test_text in test_texts:
        print(f"\nOriginal text: {test_text}")

        # Encrypt
        encrypted = encrypt(test_text, char_to_num)
        print(f"Encrypted: {encrypted}")

        # Decrypt
        decrypted = decrypt(encrypted, num_to_char)
        print(f"Decrypted: {decrypted}")

        # Verify
        if test_text == decrypted:
            print("✓ SUCCESS: Decrypted text matches original!")
        else:
            print("✗ FAILED: Decrypted text does not match original!")


def test_transformation_pattern():
    """Test that the transformation pattern is applied correctly."""
    char_to_num, num_to_char = create_character_mapping()

    # Test with 'A' (value 1) repeated to see the pattern
    # Pattern: [1, 9, 1, 6, 2, 5, 5, 2, 6, 1, 9, 1]
    # 'A' = 1, so encrypted values should be:
    # 1+1=2, 1+9=10, 1+1=2, 1+6=7, 1+2=3, 1+5=6, 1+5=6, 1+2=3, 1+6=7, 1+1=2, 1+9=10, 1+1=2, 1+1=2 (pattern repeats)

    test_text = "AAAAAAAAAAAAA"  # 13 A's to test pattern repetition
    encrypted = encrypt(test_text, char_to_num)
    expected = "2,10,2,7,3,6,6,3,7,2,10,2,2"

    print("\n" + "=" * 60)
    print("Testing Transformation Pattern")
    print("=" * 60)
    print(f"\nTest text: {test_text}")
    print(f"Encrypted: {encrypted}")
    print(f"Expected:  {expected}")

    if encrypted == expected:
        print("✓ SUCCESS: Transformation pattern is correct!")
    else:
        print("✗ FAILED: Transformation pattern is incorrect!")


if __name__ == "__main__":
    test_encryption_decryption()
    test_transformation_pattern()
