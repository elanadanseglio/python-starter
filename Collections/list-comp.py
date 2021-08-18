# 
# File: list-comp.py
# Auth: Martin Burolla
# Date: 8/17/2021
# Desc: List comprehensions
#       Works like a map() but more clear to the reader.
#       Format: [(mutate/return item) for item in items if (condition)]
#

# numbers = [1, 2, 3, 4, 5, 6]
# doubledList = [(number * 2) for number in numbers if (number % 2 == 0)]  
# print(doubledList)

# people = [
#   { "firstname": "joe", "lastname" : "smith", "age": 30 },
#   { "firstname": "peter", "lastname" : "jones", "age": 40 },
#   { "firstname": "mary", "lastname" : "jane", "age" : 50 },
# ]
# lessPeople = [(person["firstname"]) for person in people if (person["age"] > 40)]
# print(lessPeople)

# people = [
#   { "firstname": "joe", "lastname" : "smith", "age": 30 },
#   { "firstname": "sam", "lastname" : "hagar", "age": 35 },
#   { "firstname": "peter", "lastname" : "jones", "age": 40 },
#   { "firstname": "mary", "lastname" : "jane" },
# ]
# ageList = [(person["age"]) for person in people if ("age" in person and person["age"] > 30)]
# ageSum = sum(ageList)
# print(ageList, ageSum)

#
# myList = [6,2,7,3,77,7,1]
# myList.sort()
# print("Smallest Number is:", myList[0])
#