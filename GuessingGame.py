

secret_word ="cloud"
guess= ""
guess_count = 0
guess_limit = 3
out_of_guess = False
while guess!= secret_word and not(out_of_guess):
    if(guess_count < guess_limit):
        guess = input("Enter Game: ")
        guess_count+=1 #Everytime we give them a guess, we increment the guess count
    else:
        out_of_guess = True

if out_of_guess:
    print("OUT OF GUESS, YOU LOST! ")
    print(guess_count)
else:
    print("YOU WIN!")
    print(guess_count)