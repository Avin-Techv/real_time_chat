from django.http import HttpResponse
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe
from django.shortcuts import render
import json


class TextChatHome(TemplateView):
    template_name = "text_chat/index.html"


def index(request):
    return render(request, 'text_chat/index.html', {})


def room(request, room_name):
    return render(request, 'text_chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
