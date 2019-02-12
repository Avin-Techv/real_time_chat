from django.urls import path

from .views import TextChatHome

urlpatterns = [
    path('', TextChatHome.as_view(), name="home")
]
