import random
randnumber = random.randint(1,100)
print(randnumber)
userguess = None
guesses = 0
while (userguess !=randnumber):
    print("To exit enter q")
    userguess = input("Enter your guess:")
    try:
        if userguess=="q":
            print("Exited")
            exit()
        else:
            userguess=int(userguess)
            guesses +=1
            if (userguess==randnumber):
                print("you guessed it right!")
            else:
                if (userguess>randnumber):
                    print("You guessed it wrong! Enter a smaller no")
                else:
                    print("You guessed it wrong! Enter a larger no")
    except Exception as e:
        print("Invalid value")
else:
    print(f"You guessed the no in {guesses} guesses")
    with open("highscore.txt","r") as f:
        highscore = int(f.read())
    if (guesses<highscore):
        print("Boom  you broke the highscore")
        with open("highscore.txt","w") as f:
            f.write(str(guesses))
