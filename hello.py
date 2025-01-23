import hashlib
import random
import string

def generate_random_hash():
    # Generate a random 32-character string
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    # Create a hash of the random string
    hash_object = hashlib.sha256(random_string.encode())
    return hash_object.hexdigest()

# Generate hashes and check for the condition
for i in range(1000):
    hash_value = generate_random_hash()
    if hash_value.startswith('00'):
        print(f"Hash found after {i+1} iterations: {hash_value}")
        break
else:
    print("No hash starting with '00' was found in 1000 iterations.")
