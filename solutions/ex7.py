import random

num = random.randint(1, 100)

if num < 10:
    print(f"{num}: You Lose.")
elif num > 10 and num < 50:
    print(f"{num}: Try again.")
else:
    print(f"{num}: You Win!")
