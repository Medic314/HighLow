import random


def main():
    playing = True
    while playing == True:
        target = random.choice(range(101))
        player_results = determine_result(target)
        bot_results = determine_result_bot(target)
        end = end_result(player_results, bot_results)
        if end == "n":
            playing = False


def get_input():
    """get input from the user, loops if invalid"""
    input_loop = True
    while input_loop == True:
        guess = int(input("Enter a number: "))
        if guess < 0 or guess > 100:
            print("Invalid Input")
        else:
            input_loop = False
            return guess
        
def determine_result(target):
    """determines the result based on what the target is, uses get_input()"""
    guess_loop = True
    guesses = 1
    while guess_loop == True:
        guess = get_input()
        if guess == target:
            print(f"\nYou won!\nYou got it in {guesses} tries!\nThe number was {target}\n")
            guess_loop = False
            return guesses
        elif guess > target:
            print(f"{guess} is higher! Try again.")
            guesses += 1
        else:
            print(f"{guess} is lower! Try again.")
            guesses += 1

def get_input_bot(result, guesses, last_min_guess, last_max_guess):
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


def determine_result_bot(target):
    """Loops get_input() and determines the result until it is correct"""
    loop, guesses, last_max_guess, last_min_guess, result = True, 1, 100, 0, ""
    print("The bot is now guessing...")
    while loop == True:
        results = get_input_bot(result, guesses, last_min_guess, last_max_guess)
        print(results[0])
        guess = results[0]
        last_max_guess, last_min_guess = results[1], results[2]
        if guess == target:
            loop = False
            print(f"\nThe bot finished! the number was {target} and the bot got it in {guesses} tries!")
            return guesses
        if guess < target:
            guesses += 1
            result = "higher"
        else:
            guesses += 1
            result = "lower"

def end_result(user_result, bot_result):
    if user_result == bot_result:
        print(f"You and the bot tied with {user_result} guesses!")
    elif user_result > bot_result:
        print(f"You lost! You got it in {user_result} guesses, and the bot only took {bot_result}!")
    else:
        print(f"You won! The bot took {bot_result} guesses, and you only took {user_result}!")
    return play_again()

    
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