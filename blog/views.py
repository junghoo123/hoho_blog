from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import UserForm, LoginForm
from django.contrib.auth import logout

# Create your views here.
def main(request):
    return render(request, 'blog/main.html')

def photo(request):
    return render(request, 'blog/photo.html')

def login(request):
    return render(request, 'blog/login.html')

def signup(request):
    return render(request, 'blog/signup.html')

def yonghoo(request):
    return render(request, 'blog/yonghoo.html')

def junghoo(request):
    return render(request, 'blog/junghoo.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('blog/main.html')
        else:
            form = UserForm()
            return render(request, 'blog/signup.html')

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(usesrname=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main.html')
        else:
            return HttpResponse('Login failed. Try again.')
    else:
        form = LoginForm()
        return render(request, 'blog/login.html')

def signout(request):
    logout(request)
    return redirect('main.html')
