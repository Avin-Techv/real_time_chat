from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from phonenumber_field.formfields import PhoneNumberField


class UserRegisterForm(UserCreationForm):
    phone_number = PhoneNumberField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password1', 'password2']

    # def save(self, commit=True):
    #     user = super(UserRegisterForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     user.phone_number = self.cleaned_data["phone_number"]
    #     if commit:
    #         user.save()
    #     return user


class UserLoginForm(AuthenticationForm):
    username = UsernameField(label="Email",
                             widget=forms.TextInput(attrs={'type': 'email',
                                                           'autofocus': True}))

    class Meta:
        model = User
        fields = ['email', 'password']
