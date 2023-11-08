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
        print(F"Answer: {int(num1) - int(num2)}")
    if operation == "add":
        print(F"Answer: {int(num1) + int(num2)}")
    if operation == "mul":
        print(F"Answer: {int(num1) * int(num2)}")
    if operation == "div":
        if num2 == "0":
            break
        print(F"Answer: {int(num1) / int(num2)}")
        
        