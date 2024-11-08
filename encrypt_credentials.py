from cryptography.fernet import Fernet
import base64

# Generate a key for encryption and print it
def generate_key():
    key = Fernet.generate_key()
    print(f"Your encryption key (keep this safe and don't share it): {key.decode()}")
    return key

# Encrypt your credentials
def encrypt_credentials(key, credentials):
    fernet = Fernet(key)
    encrypted_credentials = {}
    for name, value in credentials.items():
        encrypted_value = fernet.encrypt(value.encode()).decode()
        encrypted_credentials[name] = encrypted_value
    return encrypted_credentials

if __name__ == "__main__":
    # Generate a key and print it for you to save securely
    key = generate_key()

    # Define your credentials
    credentials = {
        "API_KEY": "vYcnUKC4JtphMqWmPDPB419vs",
        "API_KEY_SECRET": "Da1rZwe4LwVXM1qnF7hx2QzedmE9oYcdCsgRT2F2nu3absg369",
        "BEARER_TOKEN": "AAAAAAAAAAAAAAAAAAAAAMFywwEAAAAAPn7LVfpGTLt9WKBzM8Y%2FVxbTf0A%3DQwSLx4mUPX8iuASMIVYsdtxlgm8FGArcUuXnHZimpchlqGBjnV",
        "ACCESS_TOKEN": "1695619526988111873-billasHL9yUqmJhGnQXR7YsKaoNZzy",
        "ACCESS_TOKEN_SECRET": "xNMJC17q8UVUUe3mOudBZcL7rgEgreYBA7g0IzFxOwdTx"
    }

    # Encrypt and print the credentials
    encrypted_credentials = encrypt_credentials(key, credentials)
    for name, encrypted_value in encrypted_credentials.items():
        print(f"{name}: {encrypted_value}")
