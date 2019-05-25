from django.urls import path

from . import views

app_name = 'Frontweb'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('front/', views.frontshow, name='front'),
]