from random import randint

lowest_num = 1
highest_num = 10


def play_game():
    answer = randint(lowest_num, highest_num)
    guesses = 0
    is_running = True

    print("Guessing Game")

    while is_running:
        guess = input(f"Select a number between {
                      lowest_num} and {highest_num}: ")

        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            if guess < lowest_num or guess > highest_num:
                print("Invalid guess, that number is out of range")
                print(f"Please select a number between {
                      lowest_num} and {highest_num}")
            elif guess < answer:
                print("You're under the number! Try again!")
            elif guess > answer:
                print("You're over the number! Try again!")
            else:
                print(f"You're correct! The answer is {answer}")
                print(f"Your number of guesses was {guesses}")
                is_running = False
        else:
            print("Invalid guess, this is not a number")
            print(f"Please select a number between {
                  lowest_num} and {highest_num}")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thank you for playing!")


play_game()
