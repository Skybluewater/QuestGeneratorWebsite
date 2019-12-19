from django.db import models
from login.models import User


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    score = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    if_fra = models.BooleanField(default=False)

    def __get_answer_id__(self):
        return self.answer_id

    def __answer_id_increase__(self):
        self.answer_id = self.answer_id + 1

