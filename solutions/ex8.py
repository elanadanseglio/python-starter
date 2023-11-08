myList = [6,2,7,3,77,7,1]

myMin = myList[0]
for i in range(len(myList)):
    if myList[i] < myMin:
        myMin = myList[i]
        
print(myMin)