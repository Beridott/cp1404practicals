"""
CP1404 Practical 05
Emails
Estimate: 25 mins
Actual:
"""

def main():
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        suggested_name = extract_name_from_email(email)

def extract_name_from_email(email):
