from django.urls import path

from . import views

app_name = 'Backweb'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('backweb/', views.back, name='back'),
    path('back_table/', views.back_table, name='back_table'),
    path('redirect_frontlogin/', views.redirect_frontlogin, name='redirect_frontlogin'),
    path('pages_blank/', views.pages_blank, name='pages_blank'),
    path('icon-fontawesome/', views.icon_fontawesome, name='icon_fontawesome'),

]