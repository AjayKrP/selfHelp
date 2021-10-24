from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    name = forms.CharField(label='Name')

    class Meta:
        model = User
        fields = ("username", "email", "name", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']
        if commit:
            user.save()
        return user