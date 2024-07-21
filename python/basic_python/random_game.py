import random

print("Welcome to the Random Number Guessing Game...")
guess = random.randint(1, 100)
print("You have to guess a number from 1 to 100.")
print("You will have only 10 chances, so be careful!!!")

loss = 10

while True:
    print("\n1. Play\n2. Quit")
    ask = int(input("Choose: "))

    if ask == 1:
        pred = int(input("Guess number:  "))

        while loss > 0:
            if pred == guess:
                print("Congratulations, you have won the game!!!!!\n")
                print("WINNER")
                break
            elif pred < guess:
                print("HINT: Try guessing a bigger number!")
            elif pred > guess:
                print("HINT: Try guessing a smaller number!")

            loss -= 1
            print("Chances left: ", loss)

            if loss == 0:
                print("SORRY, you have run out of chances.\nBetter luck next time.")
                break

            pred = int(input("Guess number:  "))
    else:
        print("Quitting!....")
        break
