def main():
    vowels = "aeiou"
    count = 0
    userinput = input("Enter String: ")
    
    for i in userinput:
        if i.lower() in vowels:
            count+=1
    
    print(f"Vowels: {count}")
    print(f"Consonants: {len(userinput)-count}")
    
main()