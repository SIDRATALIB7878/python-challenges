import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

def main():
    print("🔐 Simple Password Generator 🔐\n")
    
    length = int(input("Enter password length (min 8): "))
    while length < 8:
        print("❌ Password length must be at least 8!")
        length = int(input("Enter password length (min 8): "))
    
    password = generate_password(length)
    print(f"\n🔑 Generated Password: {password}\n")
    print("✅ Password generated successfully!")

if __name__ == "__main__":
    main()
