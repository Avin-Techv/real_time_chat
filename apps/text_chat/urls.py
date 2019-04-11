from django.urls import path
from .views import UserView, GroupChatView

app_name = "text_chat"

urlpatterns = [
    path('', UserView.as_view(), name="home"),
    path('group/<slug:slug>/', GroupChatView.as_view(), name="group")
]
