from django.urls import path

from .views import TextChatHome
app_name = "text_chat"

urlpatterns = [
    path('', TextChatHome.as_view(), name="home")
]
