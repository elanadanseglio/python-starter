def main():
    myList = []
    string = input("Enter list of numbers: ")

    myList = string.split(",")

    if myList[0] == myList[-1]:
        return True
    return False

print(main())