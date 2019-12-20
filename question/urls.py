from django.urls import path
from . import views

app_name = "Quest_Generator"
urlpatterns = [
    path('quest_generator/', views.generator, name="Generator"),
    path('answer/<int:num>/<int:answer_id>', views.confirm, name="Answer"),
]
