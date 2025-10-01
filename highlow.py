import random

def main():
    playing = True
    while playing == True:
        target = random.choice(range(101))
        print(target)
        end = determine_result(target)
        if end == "n":
            playing = False



def get_input():
    input_loop = True
    while input_loop == True:
        guess = int(input("Enter a number: "))
        if guess < 0 or guess > 100:
            print("Invalid Input")
        else:
            input_loop = False
            return guess
    
def play_again():
    result = input("Play again? Y/N").strip().lower()
    if result == "y":
        print("")
    else:
        print("Have a good day!")
        return "n"


def determine_result(target):
    guess_loop = True
    guesses = 1
    while guess_loop == True:
        guess = get_input()
        if guess == target:
            print(f"\nYou won!\nYou got it in {guesses} tries!\nThe number was {target}")
            guess_loop = False
            return play_again()
        elif guess > target:
            print(f"{guess} is higher! Try again.")
            guesses += 1
        else:
            print(f"{guess} is lower! Try again.")
            guesses += 1







if __name__ == "__main__":
    main()