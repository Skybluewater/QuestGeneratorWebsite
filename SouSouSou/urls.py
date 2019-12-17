from django.urls import path
from . import views

app_name = "SouSouSou"
urlpatterns = [
    path('quest_generator/', views.quest_generator, name="Generator"),
    path('', views.class_list, name="main")
]
