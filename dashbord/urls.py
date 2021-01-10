from django.urls import path
from . import views
name = 'dashbord'

urlpatterns = [path('', views.index, name='index'),]