from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('hello welcome to the backweb')

def back(request):
    return render(request, 'backend/index.html')

def back_table(request):
    return render(request, 'backend/table-basic.html')

def redirect_frontlogin(request):
    print("goodsssss!!!")

def pages_blank(request):
    return render(request, 'backend/pages-blank.html')
def icon_fontawesome(request):
    return render(request, 'backend/icon-fontawesome.html')
