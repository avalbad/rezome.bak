from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username','email','age')


class customUserChangeForm(UserChangeForm):
    model = CustomUser
    fields = UserChangeForm.Meta.fields