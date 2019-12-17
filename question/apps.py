from django.apps import AppConfig
from django.db.models.signals import post_migrate


class QuestionConfig(AppConfig):
    name = 'question'

    def ready(self):
        post_migrate.connect(do_inti_data, sender=self)


def do_inti_data(sender,**kwargs):
    from question.inti_data import inti_data
    inti_data()
