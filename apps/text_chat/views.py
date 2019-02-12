from django.views.generic import TemplateView


class TextChatHome(TemplateView):
    template_name = "text_chat/base.html"

