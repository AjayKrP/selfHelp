from django.shortcuts import render, redirect
from users.ui.forms.UserCreationForm import RegistrationForm
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home/home.html')
