from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login, logout
# Create your views here.

@csrf_exempt
def signup(request):
    if request.user.is_authenticated:
        return redirect('login')
    if request.method=='POST':
        un=request.POST.get('un')
        em=request.POST.get('em')
        pw1=request.POST.get('pw1')
        pw2=request.POST.get('pw2')
        if pw1==pw2:
            if not User.objects.filter(username=un).exists():
                User.objects.create_user(
                    username=un,
                    email=em,
                    password=pw1)
                return redirect('login')
        else:
            return render(request,'signup.html',{'msg':'password does not match!'})
    return render(request,'signup.html')

@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return redirect('notes')
    if request.method=='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        user=authenticate(request,username=un,password=pw)
        if user is not None:
            login(request,user)
            return redirect('notes') 
        else:
            return render(request,'login.html',{'msg':'Invalid Credentials!!'})
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('main')
# def home(request):
    # print(request.user.username)
    # print(request.user.email)
    # print(request.user.id)
    # return render(request,'main.html')