from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomePageView, RegistrationView, ResetPassword

# Create your views here.
app_name = "authentication"

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('login/', auth_views.LoginView.as_view(template_name="authentication/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="authentication/logout.html"), name="logout"),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('reset_password/', ResetPassword.as_view(), name="reset_password")
]
