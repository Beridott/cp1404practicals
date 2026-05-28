MIN_LENGTH = 8

def main():
    """This function will coordinate the password verification and printing."""

    password = get_password(MIN_LENGTH)
    receive_password(password)


def receive_password(password: str):
    """This function will print asterisks matching the length of the password."""
    print("*" * len(password))


def get_password(min_length: int) -> str:
    """This function will get and validate a password of a minimum length."""

    password = input("Enter password: ")

    while len(password) < min_length:
        print("Password too short!")
        password = input("Enter password: ")
    return password

main()







