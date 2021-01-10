from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest) -> HttpResponse:
    """Indexの表示

    Args:
        request (HttpRequest): HttpRequest

    Returns:
        HttpResponse: HttpResponse
    """
    return render(request, 'dashbord/index.html')