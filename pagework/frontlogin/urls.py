from django.urls import path

from . import views

app_name = 'Frontlogin'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('redirect_frontlogin/', views.redirect_frontlogin, name='redirect_frontlogin'),
    path('redirect_frontweb/', views.redirect_frontweb, name='redirect_frontweb'),

]