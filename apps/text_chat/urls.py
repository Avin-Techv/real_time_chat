from django.urls import path

from .views import UserView
app_name = "text_chat"

urlpatterns = [
    path('', UserView.as_view(), name="home")
]
