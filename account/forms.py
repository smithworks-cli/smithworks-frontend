from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        help_text="Required. Add a valid email address", required=True, max_length=80
    )

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")
