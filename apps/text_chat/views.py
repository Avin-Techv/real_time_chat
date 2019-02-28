from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe
from django.shortcuts import render
from .models import Message
import json


class TextChatHome(TemplateView):
    template_name = "text_chat/index.html"


class ChatHome(TemplateView):
    template_name = "text_chat/room.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ChatHome, self).get_context_data(*args, **kwargs)
        latest_message = Message.objects.last()
        context['last_message'] = latest_message.content
        return context


def index(request):
    return render(request, 'text_chat/index.html', {})


@login_required
def room(request, room_name):
    return render(request, 'text_chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })
