from django.urls import path

from . import views

app_name = 'page404'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('page_404/', views.page_404, name='page_404'),
]