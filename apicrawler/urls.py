from django.urls import path
from . import views

urlpatterns = [
    path('search_lenovo', views.search_lenovo, name='search_lenovo')
]
