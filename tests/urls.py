from django.http import HttpResponse
from django.template import engines
from django.urls import re_path


def show_user(request):
    content = (
        engines["django"]
        .from_string(
            "{% if user.is_authenticated %}{{ user }}"
            "{% elif user.is_anonymous %}anonymous"
            "{% else %}no user"
            "{% endif %}"
        )
        .render(request=request)
    )
    return HttpResponse(content, content_type="text/plain")


urlpatterns = [re_path(r"", show_user)]
