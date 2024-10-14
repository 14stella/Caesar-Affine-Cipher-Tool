
def caesar_encrypt(plaintext, shift_key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97  
            encrypted_text += chr((ord(char) + shift_key - shift) % 26 + shift)
        else:
            encrypted_text += char  
    return encrypted_text


def affine_encrypt(plaintext, a, b):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97  
        
            encrypted_text += chr(((a * (ord(char) - shift) + b) % 26) + shift)
        else:
            encrypted_text += char  
    return encrypted_text


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def combined_encrypt(plaintext, caesar_shift, affine_a, affine_b):
    
    caesar_encrypted = caesar_encrypt(plaintext, caesar_shift)
    print(f"Caesar Encrypted Text: {caesar_encrypted}")
    
    
    affine_encrypted = affine_encrypt(caesar_encrypted, affine_a, affine_b)
    return affine_encrypted


plaintext = input("Enter the plaintext: ")

try:
    
    caesar_shift = int(input("Enter the Caesar shift key (0-25): "))
    if not 0 <= caesar_shift <= 25:
        raise ValueError("Invalid Caesar shift key. Please enter an integer between 0 and 25.")
    
    
    affine_a = int(input("Enter the Affine 'a' key (must be coprime with 26): "))
    affine_b = int(input("Enter the Affine 'b' key: "))
    
    
    if gcd(affine_a, 26) != 1:
        raise ValueError("'a' must be coprime with 26. Please choose a valid 'a' value.")
    
except ValueError as ve:
    print(ve)
else:
    
    final_encrypted_text = combined_encrypt(plaintext, caesar_shift, affine_a, affine_b)
    print(f"Final Encrypted Text: {final_encrypted_text}")
