from django.urls import path
from django.conf.urls import url
from . import views

from .views import TextChatHome, ChatHome
app_name = "text_chat"

urlpatterns = [
    path('', TextChatHome.as_view(), name="home"),
    path('new_chat/', ChatHome.as_view(), name="chat_home"),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
