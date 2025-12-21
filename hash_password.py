import hashlib
def hash_password(password):
    password_bytes=password.encode('utf-8')
    hashed_object=hashlib.sha256(password_bytes)
    password_hash=hashed_object.hexdigest()
    return password_hash
password=input("enter your password:")
hashed_password=hash_password(password)
print(f"your hashed password is:{hashed_password}")
