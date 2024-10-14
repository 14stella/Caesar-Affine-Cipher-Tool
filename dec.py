
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
    
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def affine_decrypt(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)  
    if a_inv is None:
        raise ValueError(f"No modular inverse for a={a} under mod 26.")
    
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97  
            
            decrypted_text += chr((a_inv * (ord(char) - shift - b) % 26) + shift)
        else:
            decrypted_text += char  
    return decrypted_text


def caesar_decrypt(ciphertext, shift_key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97  
            decrypted_text += chr((ord(char) - shift_key - shift) % 26 + shift)
        else:
            decrypted_text += char  
    return decrypted_text


def combined_decrypt(ciphertext, affine_a, affine_b, caesar_shift):
    
    affine_decrypted = affine_decrypt(ciphertext, affine_a, affine_b)
    print(f"Affine Decrypted Text: {affine_decrypted}")
    
    
    caesar_decrypted = caesar_decrypt(affine_decrypted, caesar_shift)
    return caesar_decrypted


ciphertext = input("Enter the ciphertext: ")

try:
    
    affine_a = int(input("Enter the Affine 'a' key (must be coprime with 26): "))
    affine_b = int(input("Enter the Affine 'b' key: "))
    
    
    if gcd(affine_a, 26) != 1:
        raise ValueError("'a' must be coprime with 26. Please choose a valid 'a' value.")
    
    
    caesar_shift = int(input("Enter the Caesar shift key (0-25): "))
    if not 0 <= caesar_shift <= 25:
        raise ValueError("Invalid Caesar shift key. Please enter an integer between 0 and 25.")
    
except ValueError as ve:
    print(ve)
else:
    
    final_decrypted_text = combined_decrypt(ciphertext, affine_a, affine_b, caesar_shift)
    print(f"Final Decrypted Text: {final_decrypted_text}")
