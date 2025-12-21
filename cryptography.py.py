from cryptography.fernet import Fernet
key=Fernet.generate_key()
f=Fernet(key)
text=input("Enter the text:")
msg=text.encode()
encrypt_msg=f.encrypt(msg)
decrypt_msg=f.decrypt(encrypt_msg)
print("original text",encrypt_msg)
print("Decrypted msg:",decrypt_msg)
