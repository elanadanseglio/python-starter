import datetime

file = open("output.txt", "a")

date = datetime.datetime.now()

while True:
    num1 = input("Enter first integer: ")
    if num1 == "exit":
        break

    num2 = input("Enter second integer: ")
    if num2 == "exit":
        break

    operation = input("Enter operation (add, sub, mul, div):")
    if operation == "exit":
        break

    if operation == "sub":
        result = int(num1) - int(num2)
        print(f"Answer: {result}")
        file.write(
            f"""{date.strftime("%x %X %p")}: {num1} {operation} {num2} = {result}"""
        )
    if operation == "add":
        result = int(num1) + int(num2)
        print(f"Answer: {result}")
        file.write(
            f"""{date.strftime("%x %X %p")}: {num1} {operation} {num2} = {result}"""
        )

    if operation == "mul":
        result = int(num1) * int(num2)
        print(f"Answer: {result}")
        file.write(
            f"""{date.strftime("%x %X %p")}: {num1} {operation} {num2} = {result}"""
        )
    if operation == "div":
        if num2 == "0":
            break
        result = int(num1) / int(num2)
        print(f"Answer: {result}")
        file.write(
            f"""{date.strftime("%x %X %p")}: {num1} {operation} {num2} = {result}"""
        )
    file.write("\n")
file.close()