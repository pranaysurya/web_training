def play():

        global running
        running = True
        
        randnum = 100

        tries = 0

        print(randnum)
        

     
        while running:
            try:

                answer = int(input("Guess a number between 1 and 200: "))
                if answer > randnum:
                    print("\n")
                    tries += 1
                    answer = int(input("Too high! Guess again: "))

                elif answer < randnum:
                    print("\n")
                    tries += 1
                    answer = int(input("Too low! Guess again: "))

                elif answer == randnum:
                    print("That is correct! You guessed 100 in " + str(tries) + " tries.")
                    
                    run_again = input("Do you want to play again? ")
                
            except Exception as e:
                print("That is not a valid input", e)

            if run_again == "Yes" or "yes":
                print(run_again)
                play()

            else:
                print("Goodbye!")
                running = False

            
play()





