# Caesar Cipher Encryption Function
def caesar_encrypt(plaintext, shift_key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97  # Shift for uppercase/lowercase letters
            encrypted_text += chr((ord(char) + shift_key - shift) % 26 + shift)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

# Affine Cipher Encryption Function
def affine_encrypt(plaintext, a, b):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97  # Shift for uppercase/lowercase letters
            # Affine encryption formula: (a * x + b) % 26
            encrypted_text += chr(((a * (ord(char) - shift) + b) % 26) + shift)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

# GCD function to check if 'a' is coprime with 26 (for the Affine cipher)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Combined Caesar and Affine encryption
def combined_encrypt(plaintext, caesar_shift, affine_a, affine_b):
    # Step 1: Encrypt with Caesar cipher
    caesar_encrypted = caesar_encrypt(plaintext, caesar_shift)
    print(f"Caesar Encrypted Text: {caesar_encrypted}")
    
    # Step 2: Encrypt the Caesar result with Affine cipher
    affine_encrypted = affine_encrypt(caesar_encrypted, affine_a, affine_b)
    return affine_encrypted

# Taking user input for Caesar and Affine keys
plaintext = input("Enter the plaintext: ")

try:
    # Caesar cipher key input
    caesar_shift = int(input("Enter the Caesar shift key (0-25): "))
    if not 0 <= caesar_shift <= 25:
        raise ValueError("Invalid Caesar shift key. Please enter an integer between 0 and 25.")
    
    # Affine cipher key input
    affine_a = int(input("Enter the Affine 'a' key (must be coprime with 26): "))
    affine_b = int(input("Enter the Affine 'b' key: "))
    
    # Validate that 'a' is coprime with 26
    if gcd(affine_a, 26) != 1:
        raise ValueError("'a' must be coprime with 26. Please choose a valid 'a' value.")
    
except ValueError as ve:
    print(ve)
else:
    # Perform combined encryption
    final_encrypted_text = combined_encrypt(plaintext, caesar_shift, affine_a, affine_b)
    print(f"Final Encrypted Text: {final_encrypted_text}")
