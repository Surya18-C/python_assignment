
import re

def validation():

    n = int(input("Enter number of :"))

    email = [input("Enter : ") for _ in range(n)]

    valid_email = []

    for mail in email:
        pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'

        if re.match(pattern, mail):
            valid_email.append(mail)

        return valid_email

