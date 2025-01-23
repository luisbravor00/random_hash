from hello import generate_random_hash

def test_generate_random_hash():
    found = False
    for _ in range(1000):
        hash_value = generate_random_hash()
        if hash_value.startswith('00'):
            found = True
            break
    assert found, "No hash starting with '00' was found in 1000 iterations."

# Run the test
test_generate_random_hash()
print("Test passed!")