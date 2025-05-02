class Quiz_Values():

    def ask_question(self, question):

        global ui
        ui = input(question)

score = 0

class Checking(Quiz_Values):
    def check_answer(self, answer):

        try:

            attempts = 0
            incorrect = True
            while ui != str(answer) and incorrect:
                x = input("Wrong. Try again: \n")

                attempts += 1



                if x == str(answer):
                    print("That is correct!. You took {} tries.".format(attempts))
                    
                    score += 10 - attempts

                    attempts = 0
                    incorrect = False

                elif attempts == 10:
                    print("You took too many tries. you get no points for this question. \n")

                    attempts = 0
                    incorrect = False
                

            
        except Exception as e:
            print("", e)


quiz = Checking()

print("Welcome to General Knowledge Quiz!")
print("----------------------------------")
print("Answering questions correctly get you 10 points.")
print("Answering questions incorrectly gives you 1 point less for each extra attempt you have to make.")
print("If you take too many tries, you will not get any points for that question. \n \n")

questions = ["What is the capital of France? ", "What is 45 times 30? ", "What does TD in 'TD Bank' stand for? ", "What is the tallest mountain in the world? "]

answers = ["Paris", "1350", "Toronto Dominion", "Mount Everest"]

count = 0

for i in questions:


    quiz.ask_question(questions[count])
    quiz.check_answer(answers[count])

    count += 1

print("Your total score is {}.".format(score))
         


