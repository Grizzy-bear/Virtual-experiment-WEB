from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # return render(request, )
    return HttpResponse("hello, welcome to the backendlogin !!!!")

def login(request):
    return render(request, 'backendLogin/index.html')