from django.db import models
from login.models import User
from SouSouSou.models import History


# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=128, unique=True)
    answer_float = models.CharField(max_length=128)
    answer_Fraction = models.CharField(max_length=128)
    question_if_pow = models.BooleanField()
    question_if_negative = models.BooleanField()
    question_operators_num = models.IntegerField()
    c_time = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_if_correct = models.BooleanField(default=False)
    if_fra = models.BooleanField(default=False)
    answer_id = models.ForeignKey(History, on_delete=models.CASCADE)
    answer_if_answered_again = models.BooleanField(default=False)

    def __get_answer_type_id__(self):
        return self.answer_id

    def __answer_type_id_increase__(self):
        self.answer_id = self.answer_id + 1

