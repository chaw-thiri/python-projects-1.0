from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# TODO: create question bank which includes questions and answers
question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]['question'], question_data[i]['correct_answer']))
# print(type(question_bank[0]))        # check question bank

quiz = QuizBrain(question_bank)
while quiz.still_have_question():
    quiz.next_question()

final_score = quiz.score
print('You have completed the quiz.')
print(f"Your final score is {quiz.score}/{quiz.q_num}/")


