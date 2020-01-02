secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")

#first create a secret word variable
#guess variable
#guess_limit is less than the guess_count they can still guess
#out_of_guesses = Fasle is a boolean if out of gueses triggers you lose
#first situation is out of guesses using an if statement
#Then use an else statement to print You win if they succeed 