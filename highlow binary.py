import random


def main():
    playing = True
    while playing == True:
        target = random.choice(range(101))
        end = determine_result(target)
        if end == "n":
            playing = False


def get_input(result, guesses, last_min_guess, last_max_guess):
    """simple binary search to get a number based off of last values it returned"""
    if guesses == 1:
        max_guess, min_guess = 100, 0
    else:
        if result == "higher":
            min_guess, max_guess = (last_min_guess + last_max_guess) / 2, last_max_guess
        if result == "lower":
            max_guess, min_guess = (last_min_guess + last_max_guess) / 2, last_min_guess
    guess = (min_guess + max_guess) / 2
    return round(guess), max_guess, min_guess


def determine_result(target):
    """Loops get_input() and determines the result until it is correct"""
    loop, guesses, last_max_guess, last_min_guess, result = True, 1, 100, 0, ""
    while loop == True:
        results = get_input(result, guesses, last_min_guess, last_max_guess)
        print(results[0])
        guess = results[0]
        last_max_guess, last_min_guess = results[1], results[2]
        if guess == target:
            loop = False
            print(f"\nThe bot did it! the number was {target} and the bot got it in {guesses} tries!")
            return play_again()
        if guess < target:
            guesses += 1
            result = "higher"
        else:
            guesses += 1
            result = "lower"

    
def play_again():
    """asks to play again, returns n"""
    result = input("Play again? Y/N ").strip().lower()
    if result == "y":
        print("")
    else:
        print("Have a good day!")
        return "n"

if __name__ == "__main__":
    main()