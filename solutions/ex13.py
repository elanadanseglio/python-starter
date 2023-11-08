num1 = ""
num2 = ""

while True:
    num1 = input("Enter first integer: ")
    if num1 == "exit":
        break
    
    num2 = input("Enter second integer: ")
    if num2 == "exit":
        break

    print(f"Answer: {int(num1)+int(num2)}")
