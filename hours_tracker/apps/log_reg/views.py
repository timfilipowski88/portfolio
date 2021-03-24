from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import *
import bcrypt
# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.registration_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email_address = request.POST['email_address'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session['logged_user'] = user.id
        return redirect('/main/index/')


def login(request):
    errors = User.objects.login_validator(request.POST)

    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        user = User.objects.get(email_address=request.POST['email_address'])
        request.session['logged_user'] = user.id
        return redirect('main:index')


