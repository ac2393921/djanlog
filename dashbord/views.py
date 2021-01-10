from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('dashbord/index.html')
    ctx = {'title': 'Django学習ちゃんねる(仮)'}
    return HttpResponse(template.render(ctx, request))