from django.urls import path

from . import views

app_name = "Backlogin"
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login_crf/', views.login_crf, name='login_crf'),
    # path('login_redirect/', views.login_redirect, name='login_redirect'),


]