from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'username',
                                }))
    email = forms.EmailField(required=True,
                                widget=forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'id': 'email',
                                    'placeholder': 'example@holbertonschool.com'
                                }))
    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                }))
    password2 = forms.CharField(label='Confirm password',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                }))

    def clean_username(self): #validating user
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already in use')
        return username

    def clean_email(self): #validating email
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already in use')
        return email

    def clean(self): #validate passwords are the same
        cleaned_data = super().clean()

        if cleaned_data.get('password') != cleaned_data.get('password2'):
            self.add_error('password2', 'The password does not match')

    def save(self):
        return User.objects.create_user( #return object of type user (create new user)
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )
