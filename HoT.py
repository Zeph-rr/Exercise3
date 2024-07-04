import random

heads = 0
tails = 0

name = input("Who are you?\n")
print("Hello, " + name + "!")

print("Tossing a coin... ")
for round in range(1,4):
    if random.randint(1,2) == 1:
        print("Round" , round , ": Heads")
        heads += 1
    else:
        print("Round" , round , ": Tails")
        tails += 1

print("Heads: " , heads , "," , "Tails: " , tails)