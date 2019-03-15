from django.urls import path
from django.contrib.auth import views as auth_views

from apps.authentication.forms import UserLoginForm
from .views import HomePageView, RegistrationView, ResetPassword, ProfileView, UserLoginView

# Create your views here.
app_name = "authentication"
urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('login/', UserLoginView.as_view(template_name="authentication/login.html", form_class=UserLoginForm), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="authentication/logout.html"), name="logout"),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('reset_password/', ResetPassword.as_view(), name="reset_password")
]
