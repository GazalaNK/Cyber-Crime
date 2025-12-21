import re
def check_password(password):
    length_regex=re.compile(r'^.{8,}$')
    uppercase_regex=re.compile(r'[A-Z]')
    lowercase_regex=re.compile(r'[a-z]')
    digits_regex=re.compile(r'\d')
    special_regex=re.compile(r'[\w]')

    length_check=length_regex.search(password)
    uppercase_check=uppercase_regex.search(password)
    lowercase_check=lowercase_regex.search(password)
    digit_check=digits_regex.search(password)
    special_check=special_regex.search(password)

    if length_check and uppercase_check and lowercase_check and digit_check and special_check:
        return True
    else:
        return False

with open('password.txt') as f:
    for password in f:
        password=password.strip()
        if check_password(password):
            print("Valid password",password)
        else:
            print("Invalid password",password)
