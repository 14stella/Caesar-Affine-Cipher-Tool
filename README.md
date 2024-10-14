This project implements a combined encryption tool using Caesar and Affine ciphers. The tool performs encryption in a sequential manner: first applying Caesar cipher encryption and then encrypting the result with the Affine cipher. This approach showcases how combining classical cryptographic techniques can add complexity and enhance security.

How It Works
Caesar Cipher Encryption:

1. Caesar Cipher: 
   - Shifts each letter in the plaintext by a specified number of positions.
   - Non-alphabetic characters are not modified.
2. Affine Cipher:
   - Applies the formula (a * x + b) % 26  to each letter, where `a` and `b` are user-defined keys.
   - Ensures that `a` is coprime with 26 to guarantee that decryption is possible.

Validation:
Checks if the key 'a' for the Affine cipher is coprime with 26 to ensure proper decryption.
Validates Caesar cipher shift key to be within the range [0-25].

 Features

- Flexible Input: Supports both uppercase and lowercase letters, while leaving non-alphabetic characters unchanged.
- User-Defined Keys: Allows the user to input their own keys for both ciphers.
- Key Validation: Ensures the affine `a` key is coprime with 26 before proceeding with encryption.
