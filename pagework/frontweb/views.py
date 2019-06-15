from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello, welcome to the frontweb !!!")

def frontshow(request):
    return render(request,'work/index.html')