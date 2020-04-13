from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput
from account.models import Account

INPUT_CLASS = "appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5"


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        help_text="Required. Add a valid email address", required=True, max_length=80
    )

    class Meta:
        model = Account
        fields = ("email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class": INPUT_CLASS})
        self.fields["password1"].widget.attrs.update({"class": INPUT_CLASS})
        self.fields["password2"].widget.attrs.update({"class": INPUT_CLASS})
