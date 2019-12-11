import random

answer = 'Y'
while answer == 'Y':
    guessNum = random.randint(1, 20)
    tryNum = 5
    while tryNum != 0:
        try:
            inputNum = int(input("Enter Number between 1 until 20"))
            if inputNum > guessNum:
                print("Your Number is to High")
                tryNum = tryNum - 1
                print(tryNum, "attempt's lft")
                print("")
            elif inputNum < guessNum:
                print("Your Number is to Low")
                tryNum = tryNum - 1
                print(tryNum, "attempt's lft")
                print("")
            else:
                print("You're the Winner")
                tryNum = 0
        except:
            print("Please Enter a valid Number")
    else:
        print("The Number is ", guessNum)
        answer = str.upper(input("Do You want to play again? (Y/N)"))
else:
    print("GoodBye <3")
