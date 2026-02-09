import re
password=input("Enter a password:")
def password_strength(password):
    if len(password)<8:
        return "weak password"
    if not re.search("[a-z]",password):
        return "weak password:no small letter"
    if not re.search("[A-Z]",password):
        return "weak password no capital letter"
    if not re.search("[0-9]",password):
        return "weak pasword no digit"
    if not re.search("[!@#$%^&*<>?]",password):
        return "weak password no symbol"
    return "strong password"
print(password_strength(password))