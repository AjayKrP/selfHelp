from django.shortcuts import render, redirect
from users.ui.forms.UserCreationForm import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
        else:
            messages.error(request, form.errors)
        return redirect('login.home')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Hello'})


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            """
            htmly = get_template('users/email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            """
            ##################################################################
            messages.success(request, f'Your account with {username} has been created ! Please login to proceed.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'register here'})


################ login forms###################################################
def Login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            # AuthenticationForm_can_also_be_used__
            username = request.POST['username']
            password = request.POST['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                form = login(request, user)
                messages.success(request, f' welcome {username} !!')
                return redirect('home')
            else:
                print('user found')
                messages.info(request, f'account does not exit plz sign up')
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form, 'title': 'log in'})
    else:
        return redirect(request.META.get('HTTP_REFERER', 'home'))


def logout_user(request):
    messages.success(request, 'You have been successfully logout!')
    logout(request)
    return redirect('home')


def home(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request, 'users/users.html', {'users': users})
    messages.error(request, 'Please login to proceed.')
    return redirect('login')


def dashboard(request):
    studentConfig = {
        'title': 'Student Dashboard',
        'dashboard': {
            'title': 'Team Utilization Dashboard',
            'sidebar': [
                {'title': 'Book a Slot', 'url': '#'},
                {'title': 'Revisit Session', 'url': '#'},
                {'title': 'Complete Curriculum', 'url': '#'},
                {'title': 'Select a Mentor', 'url': '#'},
                {'title': 'Shop', 'url': '#'}
            ]
        }
    }

    mentorConfig = {
        'title': 'Mentor Dashboard',
        'dashboard': {
            'title': 'Team Utilization Dashboard',
            'sidebar': [
                {'title': 'Add Slot', 'url': '#'},
                {'title': 'My Students', 'url': '#'},
                {'title': 'Complete Curriculum', 'url': '#'},
            ]
        }
    }
    # TODO add condition to check either current user is Mentor/Student
    # and based on that send config to frontend.
    # For now fetching mentor flag from Url query params
    if request.GET.get('mentor', ''):
        config = mentorConfig
    else:
        config = studentConfig
    return render(request, 'dashboard/dashboard.html', config)
