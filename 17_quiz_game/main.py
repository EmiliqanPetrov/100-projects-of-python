from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [
    Question(question_data[0]['question'], question_data[0]['correct_answer']),
    Question(question_data[1]['question'], question_data[1]['correct_answer']),
    Question(question_data[2]['question'], question_data[2]['correct_answer']),
    Question(question_data[3]['question'], question_data[3]['correct_answer']),
    Question(question_data[4]['question'], question_data[4]['correct_answer']),
    Question(question_data[5]['question'], question_data[5]['correct_answer']),
    Question(question_data[6]['question'], question_data[6]['correct_answer']),
    Question(question_data[7]['question'], question_data[7]['correct_answer']),
    Question(question_data[8]['question'], question_data[8]['correct_answer']),
    Question(question_data[9]['question'], question_data[9]['correct_answer']),
    Question(question_data[10]['question'], question_data[10]['correct_answer']),
    Question(question_data[11]['question'], question_data[11]['correct_answer'])
]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()