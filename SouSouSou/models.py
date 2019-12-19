from django.db import models
from login.models import User


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()

    def __get_answer_id__(self):
        return self.answer_id

    def __answer_id_increase__(self):
        self.answer_id = self.answer_id + 1
