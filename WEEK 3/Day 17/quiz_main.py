from quiz_data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    text = q["question"]
    answer = q["correct_answer"]
    quest = Question(text,answer)
    question_bank.append(quest)
# print(question_bank)
question = QuizBrain(question_bank)
while question.still_has_question():
    question.next_question()
print(f"\nYou've completed the quiz\nYour final score was: {question.score} / {question.q_number}")
