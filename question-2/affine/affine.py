def strToarr(input: str):
    return [c for c in input]

def modInverse(a: int, m: int):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for a = {a} under mod {m}")

def enc(a: int, b: int, text: str):
    arr = strToarr(text)  
    
    num_arr = [(ord(char) - ord('a')) for char in arr]
    
    encrypted_num_arr = [(a * num + b) % 26 for num in num_arr]
    
    encrypted_text = ''.join([chr(num + ord('a')) for num in encrypted_num_arr])
    
    return encrypted_text

def dec(a: int, b: int, cipher_text: str):
    a_inv = modInverse(a, 26)  
    arr = strToarr(cipher_text)  
    
    num_arr = [(ord(char) - ord('a')) for char in arr]
    
    decrypted_num_arr = [(a_inv * (num - b)) % 26 for num in num_arr]
    
    decrypted_text = ''.join([chr(num + ord('a')) for num in decrypted_num_arr])
    
    return decrypted_text

cipher_text = enc(7, 12, "cipher")  
print("Encrypted text:", cipher_text)

decrypted_text = dec(7, 12, cipher_text) 
print("Decrypted text:", decrypted_text)

