userinput = input("Enter integer: ")
if type(userinput) == float:
    print(f"ERROR: {userinput} is not an integer.")
else:
    print(int(userinput)*-1)

