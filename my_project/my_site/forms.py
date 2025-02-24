from django.contrib.auth.forms import UserCreationForm as UserForm
from django.contrib.auth import get_user_model
from django import forms 
from django.utils.translation import gettext_lazy as _
User = get_user_model()

class UserCreationForm(UserForm):
    #email = forms.EmailField(
    #    label=_("Email"),
    #    max_length=254,
    #    widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    #)
    login = forms.CharField(
        label=_("Login"),
        max_length=50,
        widget=forms.TextInput(attrs={"autocomplete": "login"}),
    )
    password = forms.PasswordInput(
        label=_("Password"),
        max_length=50,
        widget=forms.TextInput(attrs={"autocomplete": "password"}),
    )
    class Meta(UserForm.Meta):
        model = User
        fields = ("login", "password") #fields = ("username", "email")
