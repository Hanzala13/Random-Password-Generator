import secrets
import string

def generate_password(length):
    """Generates a random password of a given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
