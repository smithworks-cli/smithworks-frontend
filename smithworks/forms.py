from django import forms
from smithworks.models import Profile


class ProfileForm(forms.ModelForm):
#     """Form definition for Profile."""

    class Meta:
#         """Meta definition for Profileform."""

        model = Profile
        fields = [
            "first_name",
            "last_name",
            "address_1",
            "address_2",
            "city",
            "state",
            "zip_code",
            "phone_number",
            "date_of_birth",
        ]
