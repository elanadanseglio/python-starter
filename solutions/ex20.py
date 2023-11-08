file = open("./input.txt", "r")

myWords = {}
for line in file:
    for word in line.split():
        if word in myWords:
            myWords[word] += 1
        else:
            myWords[word] = 1

for key in myWords:
    print(f"{key}: {myWords[key]}")