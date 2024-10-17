import base64

def encrypt(string):
    encoded_bytes = base64.b64encode(string.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decrypt(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

# Example usage
message = "U0dWc2JHOHNJSGR2Y214a0lRPT0=" 
# as a second question
# need to change the message 
