from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin
from django.views import generic
from django.contrib.auth import get_user_model


class TextChatHome(TemplateView):
    template_name = "text_chat/base.html"


class UserHomeView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'text_chat/users.html'
    login_url = 'admin/'
