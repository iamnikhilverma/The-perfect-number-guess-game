import random
randnumber = random.randint(1,100)
# print(randnumber)
userguess = None
guesses = 0

while (userguess !=randnumber):
    userguess = int(input("Enter your guess:"))
    guesses +=1
    if (userguess==randnumber):
        print("you guessed it right!")
    else:
        if (userguess>randnumber):
            print("You guessed it wrong! Enter a smaller no")
        else:
            print("You guessed it wrong! Enter a larger no")

print(f"You guessed the no in {guesses} guesses")
with open("highscore.txt","r") as f:
    highscore = int(f.read())

if (guesses<highscore):
    print("Boom  you broke the highscore")
    with open("highscore.txt","w") as f:
        f.write(str(guesses))