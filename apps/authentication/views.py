from django.views.generic import TemplateView


class AuthenticationHome(TemplateView):
    template_name = "authentication/base.html"


class RegistrationView(TemplateView):
    template_name = "authentication/registration.html"


class ResetPassword(TemplateView):
    template_name = "authentication/reset_password.html"
