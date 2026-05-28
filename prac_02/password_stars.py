MIN_LENGTH = 8  # 设定的最小密码长度

password = input("Enter password: ")

while len(password) < MIN_LENGTH:
    print("Password too short!")
    password = input("Enter password: ")

print("*" * len(password))