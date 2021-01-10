from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest) -> HttpResponse:
    """Indexの表示

    Args:
        request (HttpRequest): HttpRequest

    Returns:
        HttpResponse: HttpResponse
    """
    return render(request, 'dairy_report/index.html')

def detail(request: HttpRequest) -> HttpResponse:
    """Indexの表示

    Args:
        request (HttpRequest): HttpRequest

    Returns:
        HttpResponse: HttpResponse
    """
    return render(request, 'dairy_report/show.html')

def create(request: HttpRequest) -> HttpResponse:
    """Indexの表示

    Args:
        request (HttpRequest): HttpRequest

    Returns:
        HttpResponse: HttpResponse
    """
    return render(request, 'dairy_report/create.html')

def edit(request: HttpRequest) -> HttpResponse:
    """Indexの表示

    Args:
        request (HttpRequest): HttpRequest

    Returns:
        HttpResponse: HttpResponse
    """
    return render(request, 'dairy_report/edit.html')