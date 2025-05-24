import random

num = random.randint(1,100)
while True:
    try:
        choice = int(input("Guess the number between 1 and 100: "))
        if(choice == num): 
            print("Congratualations! You guessed the number")
            break
        elif(choice > num):
            print("Too High")
        else:
            print("Too low")
    except ValueError:
        print("Please Enter a Valid Number")