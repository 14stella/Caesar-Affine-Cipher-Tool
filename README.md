This project implements a combined encryption tool using Caesar and Affine ciphers. The tool performs encryption in a sequential manner: first applying Caesar cipher encryption and then encrypting the result with the Affine cipher. This approach showcases how combining classical cryptographic techniques can add complexity and enhance security.

How It Works
Caesar Cipher Encryption:

Shifts each letter in the plaintext by a specified number of positions.
Non-alphabetic characters remain unchanged.
Affine Cipher Encryption:Affine Cipher Encryption:

Applies the formula(a*x+b)mod26 to each letter of the text.
Uses the result from the Caesar cipher encryption as input.
Validation:

Checks if the key 'a' for the Affine cipher is coprime with 26 to ensure proper decryption.
Validates Caesar cipher shift key to be within the range [0-25].
