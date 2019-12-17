from .models import Question
from Generator.main import main


def init_data():
    if_pow = 0
    while if_pow <= 1:
        if_negative = 0
        while if_negative <= 1:
            operators = 2
            while operators < 10:
                return_list = main(5, operators, if_negative, if_pow, 9)
                i = 0
                quest: str
                answer_fraction: str
                answer_flo: str
                while i < return_list.__len__():
                    quest = return_list[i]
                    i += 1
                    answer_fraction = return_list[i]
                    i += 1
                    answer_flo = return_list[i]
                    Question.objects.create(question=quest, question_if_negative=if_negative, question_if_pow=if_pow,
                                            answer_float=answer_flo, answer_Fraction=answer_fraction)
                    print('saved')
                    i = i + 1
                operators += 1
            if_negative += 1
        if_pow += 1
    print('finished')


def inti_data():
    print('Initializing data ')
    init_data()
