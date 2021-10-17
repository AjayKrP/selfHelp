from django.shortcuts import render, redirect
from users.ui.forms.UserCreationForm import RegistrationForm
from django.contrib import messages


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
