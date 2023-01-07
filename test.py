import hashlib

# Define the string and salt
string = "nuBz6Bdhn"
salt = "j3bAdelk0"

# Convert the string and salt to bytes
string_bytes = string.encode()
salt_bytes = salt.encode()

hashed_string = hashlib.pbkdf2_hmac("sha1", string_bytes, salt_bytes, 4096)
hashed_string_hex = hashed_string.hex()
print(hashed_string_hex)
