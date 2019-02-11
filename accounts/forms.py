from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('name', 'email')

class Register(forms.Form):
    pass