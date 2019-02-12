from django.urls import path

from .views import AuthenticationHome

# Create your views here.

urlpatterns = [
    path('', AuthenticationHome.as_view(), name="authentication_home")
]
