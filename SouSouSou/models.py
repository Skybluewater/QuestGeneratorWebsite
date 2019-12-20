from django.db import models
from login.models import User
from django.utils import timezone


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    score = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    if_fra = models.BooleanField(default=False)

    def __set_end_time__(self):
        self.end_time = timezone.now()
