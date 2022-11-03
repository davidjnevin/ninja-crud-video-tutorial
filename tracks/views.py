from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    """index.

    :param request:
    :rtype: HttpResponse
    """
    return render(request, "index.html", {})
