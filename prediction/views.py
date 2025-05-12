# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        user = User.objects.create_user(username=uname, email=email, password=pwd)
        return redirect('login')
    return render(request, 'signup.html')

def index(request):
    return render(request, 'index.html')

def predict_view(request):
    if request.method == 'POST':
        # collect user inputs and process prediction here
        data = request.POST
        # model prediction logic will go here
        return render(request, 'result.html', {'result': 'Low Risk'})  # just a placeholder
    return render(request, 'predict.html')

def logout_view(request):
    logout(request)
    return redirect('login')
