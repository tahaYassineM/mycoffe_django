from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput, NumberInput
from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList


class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'username')
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'username': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('city', 'location1', 'location2', 'state', 'zip')
        widgets = {
            'city': TextInput(attrs={'class': 'form-control'}),
            'location1': TextInput(attrs={'class': 'form-control'}),
            'location2': TextInput(attrs={'class': 'form-control'}),
            'state': TextInput(attrs={'class': 'form-control'}),
            'zip': NumberInput(attrs={'class': 'form-control'})
        }
