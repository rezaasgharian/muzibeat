from django import forms

class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password_1 = forms.CharField(max_length=50)
    password_2 = forms.CharField(max_length=50)