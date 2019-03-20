from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email address is already in use.')


class UserLoginForm(AuthenticationForm):
    username = UsernameField(label="Email",
                             widget=forms.TextInput(attrs={'type': 'email',
                                                           'autofocus': True}))

    class Meta:
        model = User
        fields = ['email', 'password']
