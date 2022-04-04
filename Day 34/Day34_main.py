# Day 34 Project - Quizzler App

from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface, SetupInterface
import requests

CATEGORY_DICT = {
    "General Knowledge": 9,
    "Science": 17,
    "Geography": 22,
    "History": 23
}


def create_question_bank(num_qs, cat):
    """Creates the question bank based on the user selection of number of questions and category"""
    questions = []

    api_params = {
        "amount": num_qs,
        "category": CATEGORY_DICT[cat],
        "type": "boolean"
    }

    response = requests.get(url=f"https://opentdb.com/api.php", params=api_params)
    response.raise_for_status()

    question_data = response.json()["results"]
    print(question_data)

    for question in question_data:
        new_question = Question(question['question'], question['correct_answer'])
        questions.append(new_question)

    print(len(questions))
    return questions


setup_interface = SetupInterface()
print(setup_interface.num_qs)
print(setup_interface.cat)
question_bank = create_question_bank(setup_interface.num_qs, setup_interface.cat)

# Initialise quiz
quiz = QuizBrain(question_bank)

quiz_interface = QuizInterface(quiz)
