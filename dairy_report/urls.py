from django.urls import path
from . import views
name = 'dairy_report'

urlpatterns = [
    path('/', views.index, name='index'),
    path('/detail', views.detail, name='detail'),
    path('/create', views.create, name='create'),
    path('/edit', views.edit, name='edit'),
]