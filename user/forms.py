from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from .models import Profile


class CreateUser(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control", "id": "required"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Email", "class": "form-control", "id": "required"}
        )
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if self.user:
            if Profile.objects.filter(user=self.user).exists():
                raise ValidationError("You already have a profile.")
        return cleaned_data

    # cleaned_data return korano essential cz form.is_valid() check er shomoy clean() method o triggered hoy and tokhon custom validation logic par koira validated data return na koraile form.save() and also form er context data te bhul thakbe


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user", "salary", "designation"]
