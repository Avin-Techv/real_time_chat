from django.urls import path

from .views import AuthenticationHome, RegistrationView, ResetPassword

# Create your views here.
app_name = "authentication"

urlpatterns = [
    path('', AuthenticationHome.as_view(), name="login"),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('reset_password/', ResetPassword.as_view(), name="reset_password")
]
