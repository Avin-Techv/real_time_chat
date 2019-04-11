from django.contrib.auth.models import User
from apps.authentication.models import Profile
from apps.text_chat.models import ChatGroup
from django.views.generic import ListView, View
from braces.views import LoginRequiredMixin
from django_private_chat.models import Message


class UserView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'django_private_chat/base.html'

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.all()
        context['user_list'] = User.objects.all()
        context['message_list'] = Message.objects.all()
        return context


class GroupChatView(ListView):
    model = ChatGroup
    template_name = 'django_private_chat/dialogs.html'

    def get_context_data(self, **kwargs):
        context = super(GroupChatView, self).get_context_data(**kwargs)
        context['chat_group'] = ChatGroup.objects.all()
        return context
