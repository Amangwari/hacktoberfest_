#GUSSING NUMBER PROGRAM

'''
Make a program that has a hidden number and the user has 9 chance to guess the number untill he is not correct
alongwith tell the user frequently that the number which he guess is greater or smaller than the actual number. also
tell the number of gusses and also print number of gusses left. if the user wins tell the user in which number of
gusses he tells the right answer'''

n = 18
number_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses <= 9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 18:
        print("you enter less number please input greater number.\n")
    elif guess_number > 18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses, "no.of guesses he took to finish.")
        break
    print(9 - number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses > 9):
    print("Game Over")
