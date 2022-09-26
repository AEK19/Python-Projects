# Guessing game will be Below
# In this game users will be asked to guess a secret word, if they guess it incorrectly the game will prompt them
# ... to enter it again
# goal is to specify a looping condition
# the 'guess' that user input whether right or wrong is stored in the variable 'guess' then you check to see if the
# ... guess is equal to the secret word
# if guess is correct we are going to break out of loop
# adding a 'guess limit' sets a limit on the loop
# adding a 'guess count' counts the number of times someone guesses on the loop
# add the boolean 'out of guesses' to explain to users they
# if out of guesses is 'True' then they lost the game vice versa if they are 'False'
# now we use the 'if' condition to see if user has used all their guesses
# if guess count is less than guess limit they still have some guesses left
# implement the 'else' condition if they have more guesses to show that it is true they cannot make any more attempts
# add the 'and not' condition to show that they are not out of guesses yet and the loop continues
# the 'if' condition is added in the end to show the loop result if out of guesses and the 'else' condition is added
# ... if they win
# remember to indent
# ------>
secret_word = "zebra"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count <  guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guess, You Lose! ")
else:
    print("You Win! ")