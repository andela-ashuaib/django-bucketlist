from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'Your first name',
                                     'class': 'form-control input-lg',
                                 }))

    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={
                                    'placeholder': ' Your last name',
                                    'class': 'form-control input-lg',
                                }))
    username = forms.CharField(max_length=300,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Create unique username',
                                   'autocomplete': 'off',
                                   'class': 'form-control input-lg',
                               }))
    email = forms.EmailField(max_length=100,
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'email e.g john.doe@example.com',
                                 'autocomplete': 'off',
                                 'class': 'form-control input-lg',
                             }))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': 'Create secret password',
                                   'class': 'form-control input-lg',
                               }))
    password_conf = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput(attrs={
                                        'placeholder': 'Verify secret password',
                                        'class': 'form-control input-lg',
                                    }))


    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(
            "This user already exist in the database, please choose another username")

    def clean_email(self):
        try:
            User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(
            "This email already exist in the database, please use another email address")

    def clean(self):
        if 'password' in self.cleaned_data and 'password_conf' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_conf']:
                raise forms.ValidationError(
                    "You must type in the same password each time")
        return self.cleaned_data

    def save(self):
        new_user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        return new_user
