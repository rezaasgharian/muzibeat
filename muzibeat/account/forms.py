from django import forms
from .models import User
from django.core.mail import send_mail
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_Confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','username']

    def clean_password2(self):
        data = self.cleaned_data
        if data['password_Confirmation'] and data['password'] and data['password_Confirmation'] != data['password']:
            raise forms.ValidationError('Passwords are not the same')
        return data['password_Confirmation']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password_Confirmation'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField
    class Meta:
        model = User
        fields = ['email','username']

    def clean_password(self):
        return self.initial['password']
