from django.contrib.auth.models import User
from apps.authentication.models import Profile
from django.views.generic import ListView
from braces.views import LoginRequiredMixin
from django_private_chat.models import Message, Dialog
from django_private_chat.views import DialogListView


class UserView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'django_private_chat/base.html'

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.all()
        context['user_list'] = User.objects.all()
        context['message_list'] = Message.objects.all()
        return context
