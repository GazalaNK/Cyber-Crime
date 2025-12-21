import re
def is_valid(password):
    if len(password)<8:
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'[a-z],',password):
        return False
    if not re.search(r'/d',password):
        return False
    if not re.search(r'!@#$%^&*()<>?:'"|<>|{}[]",password):
        return False
    return true
password=input("Enter your password:")
if is_valid(password):
    print(f"Your password {Password} is Valid")
else:
    print(f"Your password {password} is invalid")
