import random
answer = input("Roll the dice? (y/n): ").lower
while(answer != "n"):
    if answer == "y":
        roll = (random.randint(1,6), random.randint(1,6))
        print(roll)
    if(answer != "y"):
        print("invalid input")
    answer = input("Roll the dice? (y/n):")
print("Thanks for playing")

