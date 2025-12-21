import random
import string
def Gp(length=8):
    all_chars=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(all_chars)for i in range(length))
    return password
pls=input("Enter the length:")

if pls:
    password_length=int(pls)
else:
    password_length=8
password=Gp(password_length)
print(f"Your Generated password is:{password}")
