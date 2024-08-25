# generate a number from 1 to 10
# input from user
# check if that input is a number 1 between 10
# check if the number is the right guess
# otherwise try again

from random import randint

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Guess a number from 1 to 10: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
        print("Invalid guess, that number is out of range")
        print(f"Please select a number between {lowest_num} and {highest_num}")
    elif guess < answer:
        print("You're under the number! Try again!")
    elif guess < answer:
        print("You're over the number! Try again!")
    else:
        print("You're correct!, the answer is {answer}")
        print(f"Your number of guesses were {guesses}")
    else:
print("Invalid guess, this is not a wordle game")
print(f"Please select a number between {lowest_num} and {highest_num}")

 is_running = False
        play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing!")
        break
