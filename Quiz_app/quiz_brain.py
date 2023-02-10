class QuizBrain:
    def __init__(self, question_list):  # question_list = question_bank
        self.q_num = 0
        self.q_list = question_list
        self.score = 0

    def still_have_question(self):
        # if self.q_num < len(self.q_list):
        #     return True
        # else:
        #     return False
        return self.q_num < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_num]  # object
        self.q_num += 1
        user_answer = input(f"Q{self.q_num} : {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('Your answer is right.')
            self.score += 1

        else:
            print('You are wrong.')
            print(f"The correct answer is : {correct_answer}")
        print(f"Your current score is : {self.score}/{self.q_num}\n")
