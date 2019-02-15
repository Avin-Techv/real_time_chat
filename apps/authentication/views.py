from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'authentication/registration.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('text_chat:home')
        return render(request, 'authentication/registration.html', {'form': form})


class AuthenticationHome(TemplateView):
    template_name = "authentication/base.html"


class ResetPassword(TemplateView):
    template_name = "authentication/reset_password.html"
