import random
import string

print("🔐 Password Generator Tool")

length = int(input("Enter password length: "))

# Characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = "".join(random.choice(characters) for i in range(length))

print("\nGenerated Strong Password:")
print(password)
