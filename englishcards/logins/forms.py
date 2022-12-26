from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Nazwa użytkownika'})
        self.fields['email'].widget.attrs.update({'placeholder': 'E-Mail'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Imię'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Nazwisko'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Hasło'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Powtórz hasło', 'cols': ''})