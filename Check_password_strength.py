import re
def check_password_strength(password):
    score=0
    suggestion=[]
    if len(password)>=8:
        score+=1
    else:
        suggestion.append("password must be at least 8 characters long\n")
    if re.search(r"[A-Z]",password):
        score+=1
    else:
        suggestion.append("password must contain a uppercase letter\n")
    if re.search(r"[a-z]",password):
        score+=1
    else:
        suggestion.append("password must contain a lowercase letter\n")
    if re.search(r"\d",password):
        score+=1
    else:
        suggestion.append("password must contain one digit\n")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]",password):
        score+=1
    else:
        suggestion.append("password must conatin a special charecter\n")
    return score,suggestion
password=input("Enter your password:")
print(check_password_strength(password))
                     
                     
