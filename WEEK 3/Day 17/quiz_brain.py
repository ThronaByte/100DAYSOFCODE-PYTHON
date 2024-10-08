class QuizBrain:
    def __init__(self, question_list):
        self.q_number = 0
        self.q_list = question_list
        self.score = 0

    def still_has_question(self):
        next_number = self.q_number
        next_question = len(self.q_list)
        if next_number < next_question:
            return True
        else:
            return False

    def next_question(self):
        cur_question = self.q_list[self.q_number]
        self.q_number +=1
        user_answer = input(f"Q.{self.q_number}. {cur_question.text}: (True/False)? ").title()
        self.check_answer(user_answer,cur_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it!")
            self.score +=1
        else:
            print("You got it wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/ {self.q_number}\n")