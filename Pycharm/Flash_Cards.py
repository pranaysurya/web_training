class Quiz_Values():

    def ask_question(self, question):

        global ui
        ui = input(question)

    def check_answer(self, answer):
            
        try:
            if ui == str(answer):
                print("That is correct!")

            elif ui != str(answer):
                print("Wrong. The correct answer is {}.".format(str(answer)))
        
        except:
            print("That is not a valid input")


quiz = Quiz_Values()

questions = ["What is the capital of France? ", "What is 45 times 30? ", "What does TD in 'TD Bank' stand for? ", "What is the tallest mountain in the world? "]

answers = ["Paris", "1350", "Toronto Dominion", "Mount Everest"]

count = 0

for i in questions:


    quiz.ask_question(questions[count])
    quiz.check_answer(answers[count])

    count += 1


         


