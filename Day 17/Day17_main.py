# Day 17 Project - Quiz Game

from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

# Create question bank
question_bank = []
for question in question_data:
    new_question = Question(question['question'], question['correct_answer'])
    question_bank.append(new_question)

# Initialise quiz
quiz = QuizBrain(question_bank)

# While there are questions in the bank, ask the user the next question
while quiz.still_has_questions():
    quiz.next_question()

print("End of questions")
print(f"Final score: {quiz.score}/{quiz.question_number}")


