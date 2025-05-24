import random

playing = True


while playing:
    computer = random.choice(["r", "p", "s"])
    choice = input("rock, paper or scissors? (r/p/s): ").lower()
    if choice == "r":
        print("You chose 🪨")
        if computer == "s":
            print("Computer chose ✂️")
            print("You Win")
        elif computer == "p":
            print("Computer chose 📃")
            print("You Lose")
        else:
            print("Computer chose 🪨")
            print("Draw")
    elif choice == "p":
        print("You chose 📃")
        if computer == "s":
            print("Computer chose ✂️")
            print("You Lose")
        elif computer == "r":
            print("Computer chose 🪨")
            print("You Win")
        else:
            print("Computer chose 📃")
            print("Draw")
    elif choice == "s":
        print("You chose ✂️")
        if computer == "r":
            print("Computer chose 🪨")
            print("You Lose")
        elif computer == "r":
            print("Computer chose 📃")
            print("You Win")
        else:
            print("Computer chose ✂️")
            print("Draw")
    else:
        print("Invalid Choice")
        continue
    resume = input("Continue?(y/n): ").lower()
    if resume == "y":
        playing = True
    elif resume == "n":
        playing = False
        break
    else:
        print("Invalid Choice")
        break