from django.contrib.auth.models import User


def contacts_available(request):
    return {'user_list': User.objects.all()}
