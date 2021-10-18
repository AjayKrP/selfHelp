from django.shortcuts import render, redirect
from users.ui.forms.UserCreationForm import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
        else:
            messages.error(request, form.errors)
        return redirect('register')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Hello'})


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('users/email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'register here'})


################ login forms###################################################
def Login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('user not found')
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('home')
        else:
            print('user found')
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form, 'title': 'log in'})


def home(request):
    users = User.objects.all()
    print(users)
    return render(request, 'users/users.html', {'users': users})
