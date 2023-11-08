import hashlib

users = {}

while (True):
    str = input("Enter username: ")
    if str == "exit":
        break
    password = input("Enter password: ")
    if password == "exit":
        break
    result = hashlib.sha256(password.encode())
    users[str] = result  
    
for key in users:
    print(f"{key} : {users[key].hexdigest()}")
     
     
