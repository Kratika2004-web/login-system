import bcrypt

# Register user
username = input("Enter username: ")
password = input("Enter password: ")

# Hash password
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

print("\nUser registered successfully!")

# Login system
print("\n--- Login ---")
login_user = input("Enter username: ")
login_pass = input("Enter password: ")

# Check password
if bcrypt.checkpw(login_pass.encode(), hashed):
    print("Login Successful!")
else:
    print("Invalid Credentials!")