from django.urls import path

from .views import UserHomeView
app_name = "text_chat"

urlpatterns = [
    path('', UserHomeView.as_view(), name="home")
]
