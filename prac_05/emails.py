"""
CP1404 Practical 05
Emails
Estimate: 25 mins
Actual:
"""

def main():
    """Enter user's name and confirm validation, output neat result"""
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        suggested_name = extract_name_from_email(email)

        confirmation = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()

        if confirmation != "" and confirmation != "y":
            name = input("Name: ").strip().title()
        else:
            name = suggested_name

        email_to_name[email] = name

        print()
        email = input("Email: ").strip()

def extract_name_from_email(email):
    """Extract and format a likely name from an email address."""
    prefix = email.split("@")[0]
    name_parts = prefix.repalce('.', ' ').replace('_', ' ').split()

    extracted_name = " ".join(name_parts).title()

    return extracted_name