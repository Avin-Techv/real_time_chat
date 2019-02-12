from django.urls import path

from .views import AuthenticationHome, RegistrationView, ResetPassword

# Create your views here.

urlpatterns = [
    path('', AuthenticationHome.as_view(), name="authentication_home"),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('reset_password/', ResetPassword.as_view(), name="reset_password")
]
