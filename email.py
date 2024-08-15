import re

def isValidEmail(email):
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.fullmatch(regex, email) is not None

email = input("Enter your email id - ")

if email and isValidEmail(email):
    try:
        username, domain = email.split('@', 1)
        print("Username -", username)
        print("Domain -", domain)
    except ValueError:
        print("Invalid Email!")
else:
    print("Invalid Email!")
