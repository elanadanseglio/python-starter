wordlist = ["Hello", "World", "in", "a", "frame"]

max = len(wordlist[0])

for word in wordlist:
    if len(word) > max:
        max = len(word)

print("*" * (max + 4))

for word in wordlist:
    if len(word) < max:
        space = " " * (max - len(word))
        print(f"* {word}{space} *")
    else:
        print(f"* {word} *")


print("*" * (max + 4))
