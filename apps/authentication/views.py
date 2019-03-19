from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import TemplateView, View
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from real_time_chat import settings


class UserLoginView(LoginView):

    def get_success_url(self):
        url = self.get_redirect_url(),
        url_front = resolve_url(settings.LOGIN_REDIRECT_URL)
        url_back = self.request.user.username
        final_url = (url_front + url_back)
        return final_url or resolve_url(settings.LOGIN_REDIRECT_URL)


class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'authentication/registration.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = self.generate_username(first_name, last_name)
            obj_id = form.save()
            user = User.objects.get(id=obj_id.id)
            user.username = username
            user.save()
            messages.success(request, f"Account created for {first_name} {last_name}!")
            return redirect('text_chat:home')
        return render(request, 'authentication/registration.html', {'form': form})

    def generate_username(self, first_name, last_name):
        username = '%s%s' % (first_name[0], last_name)
        if User.objects.filter(username=username).count() > 0:
            username = '%s%s' % (first_name, last_name[0])
            if User.objects.filter(username=username).count() > 0:
                users = User.objects.filter(username__regex=r'^%s[1-9]{1,}$' % first_name).order_by('username').values(
                    'username')
                if len(users) > 0:
                    last_number_used = map(lambda x: int(x['username'].replace(first_name, '')), users)
                    last_number_used.sort()
                    last_number_used = last_number_used[-1]
                    number = last_number_used + 1
                    username = '%s%s' % (first_name, number)
                else:
                    username = '%s%s' % (first_name, 1)
        return username


class HomePageView(TemplateView):
    template_name = "authentication/base.html"


class ResetPassword(TemplateView):
    template_name = "authentication/reset_password.html"


class ProfileView(TemplateView):
    login_required = True
    template_name = "authentication/profile.html"
