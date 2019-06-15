# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello, welcome to the page404 !!!")

def page_404(request):
    return render(request,'page404/index.html')