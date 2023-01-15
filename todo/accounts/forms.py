from django import forms
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ['email', 'password1', 'password2']

