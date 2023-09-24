print("Welcome to Flarsheim Guesser!")
choice='Y' or 'N'

while(choice == 'Y' or choice == 'y'):
    print("\nPlease think of a number between and including 1 and 100.")
    
    Remainder_Three = 0
    Remainder_Five = 0
    Remainder_Seven = 0

    Remainder_Three = int(input("\nWhat is the remainder when your number is divided by 3 ?"))
    while(Remainder_Three < 0 or Remainder_Three >= 3):
        if Remainder_Three < 0 :
            print("The value entered must be 0 or greater")
        elif Remainder_Three >= 3 :
            print("The value entered must be less than 3")

        Remainder_Three = int(input("What is the remainder when your number is divided by 3 ?"))

    Remainder_Five = int(input("\nWhat is the remainder when your number is divided by 5 ?"))
    while(Remainder_Five < 0 or Remainder_Five >= 5):
        if Remainder_Five < 0 :
            print("The value entered must be 0 or greater")
        elif Remainder_Five >= 5 :
            print("The value entered must be less than 5")

        Remainder_Five = int(input("What is the remainder when your number is divided by 5 ?"))

    Remainder_Seven = int(input("\nWhat is the remainder when your number is divided by 7 ?"))
    while(Remainder_Seven < 0 or Remainder_Seven >= 7 ):
        if Remainder_Seven < 0 :
            print("The value entered must be 0 or greater")
        elif Remainder_Seven >= 7 :
            print("The value entered must be less than 7")

        Remainder_Seven = int(input("What is the remainder when your number is divided by 7 ?"))

    for i in range(1,101):
        if (i%3 == Remainder_Three and i%5 == Remainder_Five and i%7 == Remainder_Seven):
            print('Your number was',i)
            print('How amazing is that?\n')

    choice = input('Do you want to play again? Y to continue, N to quit ==>')
    while(choice != 'Y' and choice != 'y' and choice != 'N'):
        choice = input('Do you want to play again? Y to continue, N to quit ==>')
       
