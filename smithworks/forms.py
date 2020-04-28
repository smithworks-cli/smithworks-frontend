from django import forms
from smithworks.models import Profile

INPUT_CLASS = "appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5"

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"class": INPUT_CLASS})
        self.fields["last_name"].widget.attrs.update({"class": INPUT_CLASS})
        self.fields["address_1"].widget.attrs.update({"class": INPUT_CLASS})
        self.fields["address_2"].widget.attrs.update({"class": INPUT_CLASS})
        self.fields["city"].widget.attrs.update({"class": INPUT_CLASS})
        self.fields["state"].widget.attrs.update({"class": INPUT_CLASS})
        self.fields["zip_code"].widget.attrs.update({"class": INPUT_CLASS})
        self.fields["phone_number"].widget.attrs.update({"class": INPUT_CLASS})
        self.fields["date_of_birth"].widget.attrs.update({"class": INPUT_CLASS})