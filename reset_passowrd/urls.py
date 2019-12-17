from . import views
from django.urls import path

app_name = 'reset_password'
urlpatterns = [
    path('confirm/', views.user_reset, name='reset'),
    path('reset/', views.user_confirm, name='confirm'),
    path('again/', views.post, name='again'),
    path('password/', views.user_changepass, name='password')
]