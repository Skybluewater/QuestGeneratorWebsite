from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=128, unique=True)
    answer_float = models.CharField(max_length=128)
    answer_Fraction = models.CharField(max_length=128)
    question_if_pow = models.BooleanField()
    question_if_negative = models.BooleanField()
    question_operators_num = models.IntegerField()
    c_time = models.DateTimeField(auto_now_add=True)
