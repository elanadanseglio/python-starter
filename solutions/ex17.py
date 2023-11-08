import hashlib

users = {}

while True:
    mode = input("Enter mode (add|login): ")

    if mode == "exit":
        break

    username = input("Enter username: ")
    if username == "exit":
        break

    if mode == "add":
        password = input("Enter password: ")
        if password == "exit":
            break
        result = hashlib.sha256(password.encode())
        users[username] = result

    if mode == "login":
        if username not in users:
            print("User does not exist!")
            continue
        password = input("Enter password: ")
        if password == "exit":
            break
        else:
            result = hashlib.sha256(password.encode())
            if result.hexdigest() == users[username].hexdigest():
                print("Password is correct!")
            else:
                print("Incorrect password!")

for key in users:
    print(f"{key} : {users[key].hexdigest()}")
