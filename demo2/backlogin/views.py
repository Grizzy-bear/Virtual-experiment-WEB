from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, reverse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    # return render(request, )
    return HttpResponse("hello, welcome to the backendlogin !!!!")

# @login_required


def login(request):
    if request.method == 'GET':

        return render(request, 'backendLogin/index.html')
    if request.method == 'POST':
            # user = request.POST['user']
        # pwd = request.POST['pwd']
        user = request.POST.get('user')
        pwd = request.POST.get('password')
        # if request.POST['dbsx']
        # user = UserInfo(request.POST).user
        # pwd = UserInfo(request.POST).pwd
        if user == 'admin' and pwd == 'admin':
            print(user, pwd)
            # return redirect('https://www.baidu.com')
            # return redirect(reverse('Backlogin:login_redirect'))
            return HttpResponseRedirect('/backweb/backweb') 
        else:
            return HttpResponse("请先登陆")

class UserInfo(forms.Form):
    user = forms.CharField()
    pwd = forms.CharField()
# @csrf_exempt #解决403错误
def login_crf(request):
    if request.method == 'POST':
        # user = request.POST['user']
        # pwd = request.POST['pwd']
        user = request.POST.get('user')
        pwd = request.POST.get('password')
        # if request.POST['dbsx']
        # user = UserInfo(request.POST).user
        # pwd = UserInfo(request.POST).pwd
        if user == 'admin' and pwd == 'admin':
            print(user, pwd)
            # return redirect('https://www.baidu.com')
            # return redirect(reverse('Backlogin:login_redirect'))
            return HttpResponseRedirect('/backweb/backweb') 
        else:
            return HttpResponse("请先登陆")
    return HttpResponse("hello")
        

# def login_redirect(request):
#     # pass
#     return render(request, 'backweb/index')
