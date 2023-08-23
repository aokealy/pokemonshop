from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput


# Register Form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {
            "username": None,
            "email": None,
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None

        # make email a required field
        self.fields["email"].required = True

    # email validation form
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is invalid")

        # len function updated #

        if len(email) >= 250:
            raise forms.ValidationError("Your email is too long")

        return email


# Login Form


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Update the form


class UpdateUserForm(forms.ModelForm):
    password = None

    class Meta:
        model = User
        fields = ["username", "email"]
        exclude = ["password1", "password2"]
        help_texts = {
            "username": None,
            "email": None,
        }

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        # make email a required field
        self.fields["email"].required = True

    # email verification

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if (
            User.objects.filter(email=email)
            .exclude(pk=self.instance.pk)
            .exists()
        ):
            raise forms.ValidationError("This email is invalid")

        # len function updated ###

        if len(email) >= 350:
            raise forms.ValidationError("Your email is too long")

        return email
