from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
import hashlib
# Create your views here.

def home(request):
    return render(request, 'app_general/home.html')

def about(request):
    return render(request, 'app_general/about.html')

def login(request):
    return render(request, 'app_general/login.html')

def register(request):

    if request.method == 'POST':
        username = request.POST['fname'].encode()
        password = request.POST['password1'].encode()
        confirm_password = request['password2'].encode()
        email = request['email']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')

        else:
            messages.info(request, 'Password Not Match')
            return redirect('register')

        hashed_password = hashlib.sha256(password).hexdigest()

        print(username)



    return render(request, 'app_general/register.html')

def flights(request):
    return render(request, 'app_general/flights.html')

def promo(request):
    return render(request, 'app_general/promo.html')