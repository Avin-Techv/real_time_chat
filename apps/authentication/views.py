from django.views.generic import TemplateView


class AuthenticationHome(TemplateView):
    template_name = "authentication/base.html"
